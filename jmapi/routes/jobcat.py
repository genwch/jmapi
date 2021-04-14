from fastapi import APIRouter, Depends
import models as mod


apiroute = APIRouter()
tags = ["jobcat"]
dependencies = []

router = {"route": apiroute, "tags": tags, "dependencies": dependencies}


def restore_model(name):
    import pickle
    import os
    path = os.path.join(os.getcwd(), "jobcat")
    model, data, target, score = pickle.load(
        open(os.path.join(path, "{}.pkl".format(name)), 'rb'))
    return model, data, target, score


@apiroute.post("/jobcat", response_model=mod.JobCat)
async def get_job_cat(job_desc: mod.JobDesc):
    pred = ""
    model, data, target, score = restore_model("model2")
    jobdesc=job_desc.job_desc
    # job_desc = dt.get("job_desc", "")
    # print(data, target, score, job_desc)
    for p in model.predict([jobdesc]):
        pred = p
        break
    # print(model, data, target, score)
    return {"job_cat": pred}
