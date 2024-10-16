from datetime import timedelta
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from blog import models, schemas, hashing
from blog.token import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES

def login(db: Session, req: OAuth2PasswordRequestForm = Depends()):
    user = db.query(models.User).filter(models.User.email == req.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentionals.")
    
    is_valid_user = hashing.verify_password(req.password, user.password)
    
    if is_valid_user:
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)
        return schemas.Token(access_token=access_token, token_type="bearer")
    
    return "Invalid"
    