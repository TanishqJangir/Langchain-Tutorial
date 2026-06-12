from pydantic import BaseModel

class Student(BaseModel):
    name : str
    age : int

new_student = { "name": "Tanishq", "age": 21}
student = Student(**new_student)
print(student)