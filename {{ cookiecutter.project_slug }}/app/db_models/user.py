from sqlalchemy import Boolean, Integer, Column, String

from app.db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(64), unique=True)
    email = Column(String(64), unique=True)
    password = Column(String(512))
    is_active = Column(Boolean, default=True)
