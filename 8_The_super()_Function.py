class Person:
    def __init__(self, name: str, age: int):
        self.name : str = name
        self.age : int = age

    def display(slef) -> str:
        return f"Name : {slef.name} and Age : {slef.age}"


class Teacher(Person):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

if __name__ in "__main__" :
    tech : Teacher = Teacher("sajeel", 19)
    print(tech.age)
    print(tech.name)
    print(tech.display())



print("\n")

## use dataclass

from dataclasses import dataclass

@dataclass 
class Person_2:
    name : str
    age : int

    def display(slef) -> str:
        return f"Name : {slef.name} and Age : {slef.age}"
    
 
@dataclass
class Teacher_2(Person_2):
    name : str
    age : int


if __name__ in "__main__" :
    tech_2 : Teacher_2 = Teacher_2("sajeel", 19)
    print(tech_2.age)
    print(tech_2.name)
    print(tech_2.display())
