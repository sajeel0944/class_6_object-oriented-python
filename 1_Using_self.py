class Student:
    def __init__(self, name: str, marks: float):
        self.name : str = name
        self.marks : float = marks

    def display(self) -> str:
        return (f"\nStudent Details \nName: {self.name} \nMarks: {self.marks}")
    

if __name__ in "__main__" :
    result : Student = Student("sajeel", 88.87)
    CheckResult : Student = result.display()
    print(CheckResult)




## use dataclass

from dataclasses import dataclass
 
@dataclass
class Student_2:
    name : float
    marks : float

    def display(self) -> str:
        return (f"\nStudent Details \nName: {self.name} \nMarks: {self.marks}")
    

if __name__ in "__main__" :
    result_2 : Student_2 = Student_2("sajeel", 88.87)
    CheckResult_2 : Student_2 = result_2.display()
    print(CheckResult_2)
