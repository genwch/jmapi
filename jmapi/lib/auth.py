def http_exception(status_code=200, loc=[], msg="", type=""):
    from fastapi import status, HTTPException
    if status_code == 401:
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=msg,
            headers={"WWW-Authenticate": "Bearer"},
        )
    elif status_code == 422:
        return HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=[{"loc": loc, "msg": msg, "type": type}],
            headers={"WWW-Authenticate": "Bearer"},
        )
    return HTTPException(status_code=status_code, detail=msg)
