from http.client import HTTPException

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import SessionLocal, get_db
from app.schemas.schemas import DepartmentCreate, Department
from ..curd.department_crud import get_department, create_department

router = APIRouter()

@router.get("/departments/{dep_id}", response_model=Department)
def read_department(dep_id: int, db: Session = Depends(get_db)):
    department = get_department(db, dep_id=dep_id)
    if department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return department

@router.post("/departments/", response_model=Department)
def create_new_department(department: DepartmentCreate, db: Session = Depends(get_db)):
    return create_department(db=db, department=department)
