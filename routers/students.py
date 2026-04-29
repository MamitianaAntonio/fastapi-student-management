from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, query
from starlette.status import HTTP_404_NOT_FOUND
from database import get_db
import models
import schemas

router = APIRouter(prefix="/students", tags=["students"])


@router.get("/", response_model=list[schemas.StudentResponse])
def get_all_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    students = db.query(models.Student).offset(skip).limit(limit).all()
    return students


@router.get("/{student_id}", response_model=schemas.StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(
        models.Student.id == student_id).first()
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with id {student_id} not found",
        )
    return student


@router.post(
    "/", response_model=schemas.StudentResponse, status_code=status.HTTP_201_CREATED
)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    existing_email = (
        db.query(models.Student).filter(
            models.Student.email == student.email).first()
    )
    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Email {student.email} already registered",
        )
    db_student = models.Student(**student.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
