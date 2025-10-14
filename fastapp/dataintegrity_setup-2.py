from fastapi import FastAPI, HTTPException
from sqlalchemy import Column, Integer, String, Date, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from pydantic import BaseModel
from datetime import date

# ------------------ Database Connection ------------------
DATABASE_URL = "mysql+pymysql://root:Harutla%401@127.0.0.1:3306/university"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

# ------------------ Models ------------------

class Department(Base):
    __tablename__ = "department"
    department_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    department_name = Column(String(50), nullable=False)
    students = relationship("Student", back_populates="department")


class Student(Base):
    __tablename__ = "student"
    student_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String(20), nullable=True)
    dob = Column(Date, nullable=True)
    gender = Column(String(20), nullable=True)
    email = Column(String(30), nullable=True)
    phone = Column(String(15), nullable=True)
    department_id = Column(Integer, ForeignKey("department.department_id"), nullable=True)
    department = relationship("Department", back_populates="students")

# ------------------ Schemas ------------------

class DepartmentCreate(BaseModel):
    department_name: str

    class Config:
        orm_mode = True


class StudentCreate(BaseModel):
    first_name: str | None = None
    dob: date | None = None
    gender: str | None = None
    email: str | None = None
    phone: str | None = None
    department_id: int | None = None

    class Config:
        orm_mode = True

# ------------------ FastAPI App ------------------
app = FastAPI(title="University API")

# ------------------ Department Endpoints ------------------
@app.post("/departments/", response_model=DepartmentCreate)
def create_department(department: DepartmentCreate):
    db = SessionLocal()
    db_dept = Department(department_name=department.department_name)
    try:
        db.add(db_dept)
        db.commit()
        db.refresh(db_dept)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        db.close()
    return db_dept


@app.get("/departments/")
def list_departments():
    db = SessionLocal()
    depts = db.query(Department).all()
    db.close()
    return depts

# ------------------ Student Endpoints ------------------
@app.post("/students/", response_model=StudentCreate)
def create_student(student: StudentCreate):
    db = SessionLocal()
    db_student = Student(
        first_name=student.first_name,
        dob=student.dob,
        gender=student.gender,
        email=student.email,
        phone=student.phone,
        department_id=student.department_id
    )
    try:
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        db.close()
    return db_student


@app.get("/students/")
def list_students():
    db = SessionLocal()
    students = db.query(Student).all()
    db.close()
    return [
        {
            "student_id": s.student_id,
            "first_name": s.first_name,
            "dob": s.dob,
            "gender": s.gender,
            "email": s.email,
            "phone": s.phone,
            "department_id": s.department_id,
            "department_name": s.department.department_name if s.department else None
        }
        for s in students
    ]

# ------------------ Create Tables ------------------
Base.metadata.create_all(bind=engine)
