from fastapi import APIRouter, Depends, HTTPException

from app.db.base import get_db
from app.schemas.user import UserCreate
from app import crud
from app import schemas

router = APIRouter()


@router.post('/register', response_model=schemas.User, status_code=201)
def register(user: UserCreate, db=Depends(get_db)):
    if crud.user.get_user(user.email, db):
        raise HTTPException(
            409, 'A User with this email already exists'
        )
    return crud.user.create_user(db, user)