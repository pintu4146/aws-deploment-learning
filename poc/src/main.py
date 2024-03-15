from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.model import user
from src.model import db_config
from fastapi import HTTPException

app = FastAPI()

local_session = db_config.SessionLocal()


def get_db():
    db = local_session
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/users")
def get_all_users(db: Session = Depends(get_db)):
    try:
        users = db.query(user.User).all()
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
