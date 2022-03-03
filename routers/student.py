from fastapi import APIRouter,status, HTTPException, Response
import schemas,main,models
from typing import Optional,List
from sqlalchemy.orm import joinedload


router = APIRouter(
    prefix="/student",
    tags=["students"]
)


@router.get('/', response_model=List[schemas.StudentsSchema],status_code=200)
def get_all_students():
    items=main.db.query(models.Students).options(joinedload(models.Students.courses)).all()
    return items

@router.post('/', response_model=schemas.StudentsSchema, status_code=status.HTTP_201_CREATED)
def create_an_student(item: schemas.StudentsBase):
    db_item = main.db.query(models.Students).filter(models.Students.id ==
    item.id).first()
    if db_item is not None:
       raise HTTPException(status_code=400, detail="student already exists")
    new_student = models.Students(
       f_name=item.f_name,
       l_name=item.l_name,
       id=item.id,
       GPA=item.GPA)
    main.db.add(new_student)
    main.db.commit()
    return new_student

@router.get('/{item_id}',response_model=schemas.StudentsSchema,status_code=status.HTTP_200_OK)
def get_an_student(item_id:int, response: Response):
    student = main.db.query(models.Students).filter(models.Students.id==item_id).first()
    if not student:
        response.status_code = status.HTTP_404_NOT_FOUND
    return student

@router.put('/{item_id}',response_model=schemas.StudentsBase,status_code=status.HTTP_200_OK)
def update_an_student(item_id:int,item:schemas.StudentsBase):
    item_to_update=main.db.query(models.Students).filter(models.Students.id==item_id).first()
    item_to_update.f_name=item.f_name
    item_to_update.l_name=item.l_name
    item_to_update.id=item.id
    item_to_update.GPA=item.GPA
    main.db.commit()
    return item_to_update

@router.delete('/{item_id}')
def delete_student(item_id:int):
    item_to_delete=main.db.query(models.Students).filter(models.Students.id==item_id).first()
    if item_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource Not Found")
    main.db.delete(item_to_delete)
    main.db.commit()
    return item_to_delete