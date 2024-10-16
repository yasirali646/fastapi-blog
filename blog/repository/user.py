from typing import List

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from blog import schemas, models
from .. import hashing
def create(req : schemas.User, db: Session) -> schemas.User:
    req.password = hashing.hash_password(req.password)
        
    user = db.query(models.User).filter(models.User.email == req.email).first()
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"This email address has been already taken.")
    
    user = models.User(**req.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def all(db: Session) -> List[schemas.User]:
    users = db.query(models.User).all()
    return users