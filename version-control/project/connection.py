from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base
from project import app
from fastapi import Request

engine = create_engine("postgresql://postgres:postgres@localhost:5432/postgres")
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = SessionLocal()
    response = None
    try:
         response = await call_next(request)
    finally:
        request.state.db.close()
    return response


def get_db(request: Request):
    return request.state.db
