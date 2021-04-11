from fastapi import APIRouter, Depends
from fastapi_pagination import Page, paginate, add_pagination

from .auth import oauth2_scheme
from jmapi import lib as lib

import models as mod
jobs = mod.jobs_mod(debug=True)

apiroute = APIRouter()
tags = ["jobs"]
dependencies=[Depends(oauth2_scheme)]

router={"route": apiroute, "tags": tags, "dependencies": dependencies}

@apiroute.get("/jobs", response_model=Page[jobs._model])
def get_job():
# def get_job(token: str = Depends(oauth2_scheme)):
    rtn = jobs.to_dict()
    return paginate(rtn)

@apiroute.post("/jobs", response_model=Page[jobs._model])
def post_job(job: jobs._model):
    updcols = jobs.cols(attr="updcol")
    keycols = jobs.cols(attr="key")
    upd = {j[0]: j[1] for j in job if j[0] in updcols}
    key = {j[0]: j[1] for j in job if j[0] in keycols and j[1] != None}
    upd.update(key)
    rtn, dt = jobs.upsert(upd)
    if not(rtn):
        raise lib.http_exception(
            status_code=422, loc=[upd], msg="Invalid key value")
    return paginate(dt)
