from typing import TypedDict


class Person(TypedDict):
    name : str
    age : int 

new_person: Person = {
    "name" : "Tanishq",
    'age' : 11
}

print(new_person) 