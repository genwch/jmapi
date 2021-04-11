from fastapi import FastAPI, Depends
from fastapi_pagination import add_pagination
from . import routes as rt
app = FastAPI()

for r in rt.__routes__:
    app.include_router(r.get("route"), tags=r.get("tags"), dependencies=r.get("dependencies"))

app=add_pagination(app)


# @app.get("/")
# # def home(token: str = Depends(oauth2_scheme)):
# def home():
#     jobs.insert({"job_desc": "xxx"})
#     jobs.update({"job_cde": "JD0000000002", "job_desc": "yyy"})
#     # jobs.upsert({"job_desc": "xxx"})
#     rtn = jobs.to_dict()
#     return {"data": rtn}


# # @app.get("/jobs", response_model=Page[jobs._model])
# # def get_job():
# #     rtn = jobs.to_dict()
# #     return paginate(rtn)


# @app.post("/jobs", response_model=Page[jobs._model])
# def post_job(job: jobs._model):
#     updcols = jobs.cols(attr="updcol")
#     keycols = jobs.cols(attr="key")
#     upd = {j[0]: j[1] for j in job if j[0] in updcols}
#     key = {j[0]: j[1] for j in job if j[0] in keycols and j[1] != None}
#     upd.update(key)
#     # if key != {}:
#     #     filtcond=key.copy()
#     #     print(filtcond)
#     #     filt, idx = jobs.filter(filtcond)
#     #     upd.update(key)
#     #     if idx == []:
#     #         raise lib.http_exception(
#     #             status_code=422, loc=[upd], msg="Invalid key value1")
#     rtn, dt = jobs.upsert(upd)
#     if not(rtn):
#         print("2", upd)
#         raise lib.http_exception(
#             status_code=422, loc=[upd], msg="Invalid key value")
#     return paginate(dt)


# # @app.get("/items/")
# # async def read_items(token: str = Depends(oauth2_scheme)):
# #     return {"token": token}


# @app.post("/token", response_model=mod.Token)
# async def get_token(form_data: OAuth2PasswordRequestForm = Depends()):
#     user = lib.get_user(users, {"usr_cde": form_data.username,
#                                 "password": form_data.password})
#     if user is None:
#         raise lib.http_exception(
#             status_code=401, msg="Incorrect username or password")
#     access_token = lib.create_access_token(
#         data={"sub": user.get("usr_cde")}, expires_delta=lib.get_token_exp()
#     )
#     return {"access_token": access_token, "token_type": "bearer"}


# @app.post("/me")
# async def get_current_user(token: str = Depends(oauth2_scheme)):
#     from jose import jwt, JWTError
#     credentials_exception = lib.http_exception(
#         status_code=401, msg="Could not validate credentials")
#     try:
#         payload = jwt.decode(token, lib.SECRET_KEY, algorithms=[lib.ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#         token_data = mod.TokenData(username=username)
#     except JWTError:
#         raise credentials_exception
#     user = lib.get_user(users, {"usr_cde": token_data.username})
#     if user is None:
#         raise credentials_exception
#     return {"uid": user.get("uid"), "usr_cde": user.get("usr_cde")}

# add_pagination(app)
