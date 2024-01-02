from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()



@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    # only get 10 published blogs
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}



@app.get("/blog/{blog_id}")
def show(blog_id:int):
    # fetch blog with id = blog_id
    return {'data': blog_id}



@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    # fetch comments of blog with id = id
    return {'data': {'1', '2'}}


@app.get("/about")
def about():
    return {"data": "about_page"} 


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f"Blog is created with title as {blog.title}"}