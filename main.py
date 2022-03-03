from fastapi import FastAPI
import schemas
from database import SessionLocal
from routers import course,student 


app = FastAPI()
app.include_router(course.router)
app.include_router(student.router)

db = SessionLocal()

@app.get('/')
def get_items():
    return student.get_all_students()

@app.post('/')
def create_student(item: schemas.StudentsBase):
    return student.create_an_student(item)

@app.get('/{item_id}')
def get_student(item_id:int):
    return student.get_an_student(item_id)

@app.put('/{item_id}')
def update_an_student(item_id:int,item:schemas.StudentsBase):
    return student.update_an_student(item_id,item)

@app.delete('/{item_id}')
def delete_student(item_id:int):
    return student.delete_student(item_id)

@app.post('/')
def create_course(item: schemas.CoursesBase):
    return course.create_an_course(item)


@app.get('/{id}')
def get_course(id: int):
    return course.get_an_course(id)