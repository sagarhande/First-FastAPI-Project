# FastAPI imports
from fastapi import FastAPI, Depends, status, Response, HTTPException

# sqlalchemy imports
from sqlalchemy.orm import Session

# First party imports
from .schemas import Blog
from . import models
from .database import engine, SessionLocal


app = FastAPI()

# Create a DB tables
models.Base.metadata.create_all(bind=engine)

# get DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/blogs", status_code=status.HTTP_201_CREATED)
def create(request: Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(
        title=request.title,
        brief=request.brief,
        body=request.body,
        published=request.published,
    )

    db.add(new_blog)
    db.commit()

    db.refresh(new_blog)
    return new_blog


@app.get("/blogs", status_code=status.HTTP_200_OK)
def all(db: Session = Depends(get_db)):

    blogs = db.query(models.Blog).all()
    return blogs


@app.get("/blogs/{id}", status_code=status.HTTP_200_OK)
def single(
    id: int,
    response: Response,
    db: Session = Depends(get_db),
):

    blog = db.query(models.Blog).get(id)
    # blog = db.query(models.Blog).filter(models.Bolg.id = id).first()

    # if not blog:
    #     response.status_code = status.HTTP_404_NOT_FOUND
    #     return {"detail": f"Blog with {id} is not available"}

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with {id} is not available",
        )

    return blog
