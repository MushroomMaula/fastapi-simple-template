from pydantic import BaseModel


class ORMBase(BaseModel):
    class Config:
        orm_mode = True
