import contextlib

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from .base_class import Base
from app.db_models.user import User
from app.core import Config

engine = create_engine(Config.database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Session:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def create_all():
    Base.metadata.create_all(bind=engine)


def reset_db():
    with contextlib.closing(engine.connect()) as con:
        trans = con.begin()
        for table in reversed(Base.metadata.sorted_tables):
            con.execute(table.delete())
        trans.commit()
