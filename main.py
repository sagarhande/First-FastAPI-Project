from fastapi import FastAPI
from typing import Union

app = FastAPI()


@app.get("/blogs")
def blogs(limit: int = 10, published: bool = True, sort: Union[bool, None] = False):
    # Fetch all blogs from DB and return
    if published:
        return {"data": f"{limit} published blogs from DB with sorting is {sort}"}
    else:
        return {"data": f"{limit} unpublished blogs from DB with sorting is {sort}"}


@app.get("blogs/unpublished/")
def unpublished_blogs():
    # Featch all unpublished blogs
    # Should be accessible to ADMIN user
    return {"data": {"1": "unpublished-1", "2": "unpublished-2"}}


@app.get("/blogs/{id}")
def show_blog(id: int):
    # Fetch a single blog with id=id

    return {"data": id}


@app.get("/blogs/{id}/comments")
def comments(id):
    # Fetch all comments of blog with id=id

    return {"data": ["comment1", "comment2"]}
