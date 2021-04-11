import pddb


class comments_mod(pddb.pdtbl):
    def init_obj(self) -> dict:
        acl = pddb.ACL.SHARED
        # acl = pddb.ACL.PRIVATE
        path = "./data/comments.parquet"
        obj = {"cid": {"type": str, "uuid": True, "ignupd": True, "key": True},
               "job_cde": {"type": str},
               "comment_desc": {"type": str, "require": True},
               "comment_rate": {"type": str},
               "status": {"type": bool, "default": True}}
        return (obj, path, acl)
