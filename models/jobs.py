import pddb


class jobs_mod(pddb.pdtbl):
    def init_obj(self) -> dict:
        acl = pddb.ACL.SHARED
        # acl = pddb.ACL.PRIVATE
        path = "./data/jobs.parquet"
        obj = {"jid": {"type": str, "uuid": True, "ignupd": True},
               "job_cde": {"type": str, "key": True, "genrun": "JD!!cnt-10!!"},
               "company": {"type": str},
               "title": {"type": str},
               "scope": {"type": str},
               "requirement": {"type": str},
               "experience": {"type": str},
               "amount": {"type": str},
               "period": {"type": str},
               "job_cat": {"type": str},
               "status": {"type": bool, "default": True}}
        return (obj, path, acl)
