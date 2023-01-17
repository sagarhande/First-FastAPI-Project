# FastAPI imports
from fastapi import FastAPI

# First party imports
from .models import Blog

app = FastAPI()


@app.post("/blog")
def create_blog(blog: Blog):
    return blog
