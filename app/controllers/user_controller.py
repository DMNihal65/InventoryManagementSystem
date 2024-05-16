from http.client import HTTPException

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import SessionLocal, get_db
from app.schemas.schemas import UserCreate, User
from ..curd.user_crud import get_user, create_user

router = APIRouter()

@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/users/", response_model=User)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)
