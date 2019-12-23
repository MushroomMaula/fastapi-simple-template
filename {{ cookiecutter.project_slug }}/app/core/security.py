from fastapi_login import LoginManager
from app.core import Config


manager = LoginManager(Config.secret, tokenUrl='/auth/login')


def hash_password(plain_password):
    return manager.pwd_context.hash(plain_password)


def verify_password(plain_password, hashed_password):
    return manager.pwd_context.verify(plain_password, hashed_password)
