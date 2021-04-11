from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from jmapi import lib as lib

import models as mod
users = mod.users_mod(debug=False)
# if users.count() == 0:
#     rtn = users.upsert({"usr_cde": "test", "password": "test"})
#     if rtn:
#         users.save()
users.upsert({"usr_cde": "system", "password": "system"})

apiroute = APIRouter()
tags = ["auth"]
dependencies = []

router = {"route": apiroute, "tags": tags, "dependencies": dependencies}

SECRET_KEY = "JMAPI_SECRET"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(data: dict, expires_delta=None):
    from datetime import datetime, timedelta
    from jose import jwt
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_user(users, filt: dict):
    users.load()
    users.upsert({"usr_cde": "system", "password": "system"})
    df, idx = users.filter(filt)
    if df.empty:
        return None
    for d in users.to_dict(df):
        return d
    return None


def get_token_exp():
    from datetime import timedelta
    return timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)


@apiroute.post("/token", response_model=mod.Token)
async def get_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user(users, {"usr_cde": form_data.username,
                            "password": form_data.password})
    if user is None:
        raise lib.http_exception(
            status_code=401, msg="Incorrect username or password")
    access_token = create_access_token(
        data={"sub": user.get("usr_cde")}, expires_delta=get_token_exp()
    )
    return {"access_token": access_token, "token_type": "bearer"}


def token2user(token: str):
    from jose import jwt, JWTError
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
    except:
        return None
    return username


@apiroute.post("/me")
async def get_current_user(token: str = Depends(oauth2_scheme)):
    from jose import jwt, JWTError
    credentials_exception = lib.http_exception(
        status_code=401, msg="Could not validate credentials")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = mod.TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(users, {"usr_cde": token_data.username})
    if user is None:
        raise credentials_exception
    return {"uid": user.get("uid"), "usr_cde": user.get("usr_cde")}
