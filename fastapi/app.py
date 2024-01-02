from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

app = FastAPI()


students ={
    
    1:{'name':"Arun",
       'age':30,
       'class':'arts'},
    2:{'name':"user",
       'age':23,
       'class':'science'}
}



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/get_student/{student_id}")
def get_student(student_id:int):
    return students[student_id]

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}