from .base import ORMBase
from pydantic import BaseModel


class User(ORMBase):
    id: str
    email: str
    username: str


class UserCreate(BaseModel):
    email: str
    username: str
    password: str
