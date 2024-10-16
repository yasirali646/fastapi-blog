from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .. import schemas
from ..database import get_db
from ..repository import user as user_repo

router = APIRouter(
    tags=["User"],
    prefix="/User"
)

@router.post("/", status_code = status.HTTP_201_CREATED)
def create(req : schemas.User, db: Session = Depends(get_db)) -> schemas.User:
    return user_repo.create(req, db)


@router.get('/', status_code=status.HTTP_200_OK)
def all(db: Session = Depends(get_db)) -> List[schemas.User]:
    return user_repo.all(db)