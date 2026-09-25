from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.api.routers.users import router



app=FastAPI()
app.include_router(router)
    