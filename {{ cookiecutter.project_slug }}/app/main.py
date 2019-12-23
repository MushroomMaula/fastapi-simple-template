from fastapi import FastAPI, Security
from app.api import auth, user

app = FastAPI()

app.include_router(
    auth.router,
    prefix='/auth',
    tags=["auth"]
)


app.include_router(
    user.router,
    prefix='/user',
    tags=["users"]
)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
