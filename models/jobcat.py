from typing import Optional
from pydantic import BaseModel


class JobCat(BaseModel):
    job_cat: str

class JobDesc(BaseModel):
    job_desc: str
