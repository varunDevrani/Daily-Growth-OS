from sqlalchemy.orm import Session
from src.models.user import User
from src.utils.hashing import hash_password
from fastapi import HTTPException,status

def signup_user(
    db: Session,
    email: str,
    password: str
):
    #here i am Checking  duplicate user in the db
    if db.query(User).filter(User.email == email).first():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="user already exists"
        )
    #here its Hashes only plain password 
    hashed_password = hash_password(password)

    #creating user in db
    user = User(
        email=email,
        password_hash=hashed_password
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user