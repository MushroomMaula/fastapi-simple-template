from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException

from app.core.security import manager, verify_password
from app import crud
from app.db.base import get_db

router = APIRouter()


@router.post('/login')
def login(data: OAuth2PasswordRequestForm = Depends(), db=Depends(get_db)):
    email = data.username
    password = data.password
    user = crud.user.get_user(email, db)
    if not user:
        raise InvalidCredentialsException
    elif not verify_password(password, user.password):
        raise InvalidCredentialsException

    access_token = manager.create_access_token(
        data={'sub': user.email}
    )
    return {'access_token': access_token, 'token_type': 'Bearer'}



