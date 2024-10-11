from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# In-memory storage for simplicity
students_db = {}
student_id_counter = 1  # Auto-incrementing counter for student IDs

# Pydantic model for Student data
class Student(BaseModel):
    id: Optional[int] = None  # ID will be auto-assigned
    name: str
    age: int
    gender: str
    Class: str
    address: str
    contact_info: str

# Pydantic model for Partial Update (all fields optional)
class StudentUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    Class: Optional[str] = None
    address: Optional[str] = None
    contact_info: Optional[str] = None

# Create (Add) a new student
@app.post("/students/", response_model=Student)
def create_student(student: Student):
    global student_id_counter
    student.id = student_id_counter
    students_db[student_id_counter] = student
    student_id_counter += 1  # Increment the counter for the next student
    return student

# Read (Retrieve) all students
@app.get("/students/", response_model=List[Student])
def get_students():
    return list(students_db.values())

# Read (Retrieve) a specific student by ID
@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
    student = students_db.get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# Partial Update a student by ID
@app.patch("/students/{student_id}", response_model=Student)
def update_student(student_id: int, student_data: StudentUpdate):
    student = students_db.get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    # Manually update only the fields that are provided in the request
    if student_data.name != 'string':
        student.name = student_data.name
        print(student_data.name)
    if student_data.age != 0:
        student.age = student_data.age
        print(student_data.age)
    if student_data.gender != 'string':
        student.gender = student_data.gender
        print(student_data.gender)
    if student_data.Class != 'string':
        student.Class = student_data.Class
        print(student_data.Class)
    if student_data.address != 'string':
        student.address = student_data.address
        print(student_data.address)
    if student_data.contact_info != 'string':
        student.contact_info = student_data.contact_info
        print(student_data.contact_info)

    students_db[student_id] = student  # Save the updated student
    return student

# Delete a student by ID
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    student = students_db.pop(student_id, None)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}
