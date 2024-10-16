from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from ..database import get_db
from ..repository import auth


router = APIRouter(
    tags=["Authentication"]
)

@router.post("/login", status_code=status.HTTP_200_OK)
def login(db: Session = Depends(get_db), req: OAuth2PasswordRequestForm = Depends()):
    return auth.login(db, req)