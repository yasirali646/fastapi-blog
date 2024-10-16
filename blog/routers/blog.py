from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from blog import schemas
from ..database import get_db
from ..repository import blog as blog_repo
from blog.oauth2 import get_current_user

router = APIRouter(
    tags=['Blog'],
    prefix="/blog"
)

@router.post("/", status_code = status.HTTP_201_CREATED)
def create(req: schemas.Blog, db: Session = Depends(get_db),  _: schemas.User = Depends(get_current_user)):
    return blog_repo.create(req, db)


@router.get("/", status_code = status.HTTP_200_OK)
def all(db: Session = Depends(get_db),  _: schemas.User = Depends(get_current_user)) -> List[schemas.Blog]:
    return blog_repo.all(db)

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.Blog)
def show(id, db: Session = Depends(get_db),  _: schemas.User = Depends(get_current_user)):
    return blog_repo.show(id, db)


@router.delete("/{id}", status_code = status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db),  _: schemas.User = Depends(get_current_user)):
    return blog_repo.destroy(id, db)

@router.put("/{id}", status_code = status.HTTP_200_OK)
def update(id, req: schemas.Blog, db: Session = Depends(get_db),  _: schemas.User = Depends(get_current_user)):
    return blog_repo.update(id, req, db)