from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from blog import schemas, models

from typing import List


def create(req, db: Session) -> models.Blog:
    new_blod = models.Blog(**req.model_dump())
    db.add(new_blod)
    db.commit()
    return new_blod

def all(db: Session) -> List[schemas.Blog]:
    blogs = db.query(models.Blog).all()
    return blogs

def show(id, db: Session) -> models.Blog:
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with {id} is not available")
    return blog


def destroy(id, db: Session) -> models.Blog:
    record = db.query(models.Blog).filter(models.Blog.id == id)
    if not record.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with {id} is not available")
    
    record.delete(synchronize_session=False)
    db.commit()
    return "done"


def update(id, req: schemas.Blog, db: Session) -> models.Blog:
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()    
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with {id} is not available")
    
    blog.title = req.title
    blog.body = req.body
    db.commit()
    return blog

