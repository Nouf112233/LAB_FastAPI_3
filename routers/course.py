from fastapi import APIRouter,status, HTTPException, Response
import schemas,main,models
from typing import Optional,List
from sqlalchemy.orm import joinedload


router = APIRouter(
    prefix="/course",
    tags=["courses"]
)


@router.get('/', response_model=List[schemas.CoursesSchema],status_code=200)
def get_all_courses():
    items=main.db.query(models.Courses).options(joinedload(models.Courses.students)).all()
    return items

@router.post('/', response_model=schemas.CoursesBase, status_code=status.HTTP_201_CREATED)
def create_an_course(item: schemas.CoursesBase):
    db_item = main.db.query(models.Courses).filter(models.Courses.course_id ==
    item.course_id).first()
    if db_item is not None:
       raise HTTPException(status_code=400, detail="course already exists")
    new_course = models.Courses(
       course_name = item.course_name,
       course_hours = item.course_hours,
       course_id = item.course_id,
       course_description= item.course_description)
    main.db.add(new_course)
    main.db.commit()
    return new_course

@router.get('/{item_id}',response_model=schemas.CoursesSchema,status_code=status.HTTP_200_OK)
def get_an_course(item_id:int, response: Response):
    course = main.db.query(models.Courses).filter(models.Courses.id==item_id).first()
    if not course:
        response.status_code = status.HTTP_404_NOT_FOUND
    return course