import pytest
from starlette.testclient import TestClient

from app.main import app
from app.schemas import UserCreate
from app.tests.utils import fake, random_string
from app.db.base import create_all, SessionLocal, reset_db


@pytest.fixture(autouse=True)
def _():
    create_all()


@pytest.fixture(scope="session")
def db():
    db = SessionLocal()
    yield db
    db.close()
    # clear all tables
    reset_db()


@pytest.fixture()
def client():
    return TestClient(app)


@pytest.fixture()
def user_data():
    return UserCreate(
        username=fake.user_name(),
        email=fake.email(),
        password=random_string()
    )
