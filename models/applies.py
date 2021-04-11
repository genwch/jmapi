import pddb


class applies_mod(pddb.pdtbl):
    def init_obj(self) -> dict:
        acl = pddb.ACL.SHARED
        # acl = pddb.ACL.PRIVATE
        path = "./data/applies.parquet"
        obj = {"aid": {"type": str, "uuid": True, "ignupd": True, "key": True},
               "job_cde": {"type": str},
               "status": {"type": bool, "default": True}}
        return (obj, path, acl)
