from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import UserResponse, UserInput
from app.crud.users import fetch_user, fetch_users, create_users, update_users, delete_users
from typing import List


router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=List[UserResponse])
def get_users(db: Session = Depends(get_db)):
    all_users = fetch_users(db)
    return all_users


@router.get("/{id}", response_model=UserResponse)
def get_user(id: int, db = Depends(get_db)):
    user = fetch_user(id, db)
    return user


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(post: UserInput, db: Session = Depends(get_db)):
    post_dict = post.model_dump()
    new_user = create_users(post_dict, db)
    return new_user


@router.put("/{id}", response_model=UserResponse)
def update_user(id: int, post: UserInput, db: Session = Depends(get_db)):
    post_dict = post.model_dump()
    updated_user = update_users(id, post_dict, db)
    return updated_user


@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, db: Session = Depends(get_db)):
    delete_users(id, db)
    return {"message": f"User with id {id} has been deleted successfully."}