# FastAPI imports
from fastapi import FastAPI, Depends

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


@app.post("/blogs")
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


@app.get("/blogs")
def all(db: Session = Depends(get_db)):

    blogs = db.query(models.Blog).all()
    return blogs


@app.get("/blogs/{id}")
def single(id: int, db: Session = Depends(get_db)):

    blog = db.query(models.Blog).get(id)
    # blog = db.query(models.Blog).filter(models.Bolg.id = id).first()
    return blog
