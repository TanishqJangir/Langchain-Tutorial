from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name : str
    age : Optional[int] = None
    email: EmailStr
    cgpa : float = Field(gt=0, lt=10, default=4, description="A decimal Value representing the cgpa of the student.")

new_student = {"name" :"Tanishq", "age":22, "email":"tanishqjangir@gmail.com"}
student = Student(**new_student)
student_dict = dict(student)

print(student_dict)

student_json = student.model_dump_json()

print(student_json)