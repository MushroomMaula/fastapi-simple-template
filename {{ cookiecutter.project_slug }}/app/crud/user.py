from typing import Optional

from sqlalchemy.orm import Session

from app.core.security import manager, hash_password
from app.db.base import User, SessionLocal
from app import schemas


@manager.user_loader
def get_user(email: str, db: Session = None) -> Optional[User]:
    # when used by the manager no db session is passed
    if db is None:
        db = SessionLocal()
    user = db.query(User).filter(User.email == email).first()
    if db is None:
        db.close()
    return user


def create_user(db: Session, user_in: schemas.UserCreate):
    user_in.password = hash_password(user_in.password)
    user = User(**user_in.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
