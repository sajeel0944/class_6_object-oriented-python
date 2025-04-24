class Employee:
    def __init__(self, name: str, salary : int, ssn: str):
        self.name : str = name
        self._salary : int = salary
        self.__ssn : str = ssn


if __name__ in "__main__" :
    emp : Employee = Employee("sajeel", 30000, "123-97-6546")

    print(f"Name: {emp.name}")

    print(f"Salary: {emp._salary}")

    try:
        print(f"ssn: {emp.__ssn}")
    except AttributeError as e:
        print("private variable does not Directly accessible")



print("\n")


## use dataclass

from dataclasses import dataclass

@dataclass
class Employee_2:
    name : str 
    _salary : int
    __ssn : str

 
if __name__ in "__main__" :
    emp_2 : Employee_2 = Employee_2("sajeel", 30000, "123-97-6546")

    print(f"Name: {emp_2.name}")

    print(f"Salary: {emp_2._salary}")

    try:
        print(f"ssn: {emp_2.__ssn}")
    except AttributeError as e:
        print("private variable does not Directly accessible")
