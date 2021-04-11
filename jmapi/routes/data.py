from abc import ABC
from fastapi_pagination import Page, paginate, add_pagination
from typing import Optional
from fastapi import APIRouter, Depends
from .auth import oauth2_scheme, token2user
import models as mod
from jmapi import lib as lib


class data_rt(ABC):
    def __init__(self, mod_name, debug=False):
        self.__mod_name = mod_name
        self.__data_mod = mod.__model__.get(mod_name)
        self.debug = debug
        self.data_mod = self.__data_mod(debug=self.debug)
        self.model = self.data_mod._model
        self.router = self.set_route()

    def get(self, token: str = Depends(oauth2_scheme), code: Optional[str] = None):
        owner = token2user(token)
        self.data_mod.set_owner(owner)
        filt = {}
        if code != None:
            keycols = self.data_mod.cols(attr="key")
            filt = {c: code for c in keycols}
        df = self.data_mod.select(filt)
        if df.empty:
            return paginate([])
        rtn = self.data_mod.to_dict(df)
        return paginate(rtn)

    def post(self, token: str = Depends(oauth2_scheme), code: Optional[str] = None, data: dict = {}):
        owner = token2user(token)
        self.data_mod.set_owner(owner)
        updcols = self.data_mod.cols(attr="updcol")
        keycols = self.data_mod.cols(attr="key")
        if code != None:
            data.update({c: code for c in keycols})
        upd = {k: v for k, v in data.items() if k in updcols}
        key = {k: v for k, v in data.items() if k in keycols and v != None}
        upd.update(key)
        rtn, dt = self.data_mod.upsert(upd)
        if not(rtn):
            raise lib.http_exception(
                status_code=422, loc=[], msg="Invalid key value")
        self.data_mod.save()
        return paginate(dt)

    def set_route(self):
        tags = [self.__mod_name]
        # dependencies = [Depends(oauth2_scheme)]
        dependencies = None
        path = "/{}".format(self.__mod_name)
        pathwithpara = "%s/{code}" % (path)
        apiroute = APIRouter(tags=tags, dependencies=dependencies)
        apiroute.add_api_route(
            path=path, methods=["get"], name=f"Get {self.__mod_name}",
            endpoint=self.get, response_model=Page[self.model])
        apiroute.add_api_route(
            path=pathwithpara, methods=["get"], name=f"Get {self.__mod_name}",
            endpoint=self.get, response_model=Page[self.model])
        apiroute.add_api_route(
            path=path, methods=["post"], name=f"Post {self.__mod_name}",
            endpoint=self.post, response_model=Page[self.model])
        apiroute.add_api_route(
            path=pathwithpara, methods=["post"], name=f"Post {self.__mod_name}",
            endpoint=self.post, response_model=Page[self.model])
        return {"route": apiroute}
