from cgitb import text
from typing import Optional,List
from fastapi import FastAPI,status, HTTPException, Response
from pydantic import BaseModel
from sqlalchemy import TEXT
from database import SessionLocal

class StudentsBase(BaseModel):
    f_name: str
    l_name: str
    id: int
    GPA: float

    class Config:  # serialize our sql obj to json
        orm_mode = True

class CoursesBase(BaseModel):
    course_name : str
    course_hours : float
    course_id : int
    course_description: TEXT

    class Config:
        orm_mode = True

class StudentsSchema(StudentsBase):
    courses: List[CoursesBase]

class CoursesSchema(CoursesBase):
    students: List[StudentsBase]