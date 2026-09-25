from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import UserCreate, UserResponse
from app.models.user import User as User_table
from typing import List

router=APIRouter(prefix="/users", tags=["Users"])

@router.post("/create_user", response_model=UserResponse)
def create_user(user: UserCreate ,db: Session=Depends(get_db)):
    new_user=User_table(**user.model_dump())

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get("/view_users", response_model=List[UserResponse])
def view_users(db: Session=Depends(get_db)):
    users=db.query(User_table).all()
    if not users:
        raise HTTPException(status_code=404, detail="no user found")
    return users

@router.delete("/clear_users")
def delete_users(db: Session=Depends(get_db)):
    db.query(User_table).delete()
    db.commit()
    return {"message": "All Users Deleted"}

@router.delete("/delete_one")
def delete_a_user(id: int, db: Session=Depends(get_db)):
    user=db.query(User_table).filter(User_table.id==id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User does not exist")
    db.delete(user)
    db.commit()
    return {"message": f"User {id} deleted"}

@router.put("/update_user", response_model=UserResponse)
def update_user(user: UserCreate, id: int, db: Session=Depends(get_db)):
    db_user=db.query(User_table).filter(User_table.id==id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="No matching user")
    updates=user.model_dump()
    for key, value in updates.items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/view_user_by_id", response_model=UserResponse)
def view_user_by_id(id: int, db: Session=Depends(get_db)):
    user=db.query(User_table).filter(User_table.id==id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found!")
    return user