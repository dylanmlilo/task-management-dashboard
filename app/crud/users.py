from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models import User


def fetch_users(db: Session):
    users = db.query(User).all()
    return users


def fetch_user(id: int, db: Session):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id of {id} was not found")
    return user

def create_users(post, db: Session):
    new_user = User(**post)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def update_users(id, post, db: Session):
    user = db.query(User).filter(User.id == id).first()
    
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id of {id} was not found")
    
    for key, value in post.items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)

    return user

def delete_users(id, db: Session):
    user = db.query(User).filter(User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id of {id} was not found")
    
    db.delete(user)
    db.commit()

    return  HTTPException(status_code=status.HTTP_204_NO_CONTENT)
