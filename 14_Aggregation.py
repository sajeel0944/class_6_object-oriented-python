class Employee:
    def __init__(self, name: str):
        self.name : str = name

    def get_info(self) -> str:
        return f"Employee: {self.name}"
    
class Department:

    def __init__(self,  employee: Employee):
        self.employee : Employee = employee

    def get_employee_info(self) -> str:
        return self.employee.get_info()
    
if __name__ in "__main__" :
    emp : Employee = Employee("sajeel")
    dept : Department = Department(emp)
    print(dept.get_employee_info())

       
        

## use dataclass

from dataclasses import dataclass

@dataclass

class Employee:
    name : str

    def get_info(self) -> str:
        return f"Employee: {self.name}"
    

@dataclass  
class Department:
    employee : Employee 

    def get_employee_info(self) -> str:
        return self.employee.get_info()
    
if __name__ in "__main__" :
    emp : Employee = Employee("sajeel")
    dept : Department = Department(emp)
    print(dept.get_employee_info())

       