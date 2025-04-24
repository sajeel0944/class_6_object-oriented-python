class Engine:
    def __init__(self, horsepower : int):
        self.horsepower : int = horsepower

    def start(self) -> str:
        return f"Engine with {self.horsepower} horsepower started!"
    

class Car:
    def __init__(self, brand : str, engine : Engine):
        self.brand : str = brand
        self.engine : Engine = engine

    def start_engine(self) -> str:
        return self.engine.start()
    
if __name__ in "__main__" :
    engi : Engine = Engine(100)
    car : Car = Car("Toyota", engi)
    print(car.start_engine())




## use dataclass

from dataclasses import dataclass

@dataclass
class Engine_2:
    horsepower : int

    def start(self) -> str:
        return f"Engine with {self.horsepower} horsepower started!"
    

@dataclass
class Car_2:
    brand : str
    engine : Engine
   
    def start_engine(self) -> str:
        return self.engine.start()
    
if __name__ in "__main__" :
    engi_2 : Engine_2 = Engine_2(100)
    car_2 : Car_2 = Car_2("Toyota", engi)
    print(car_2.start_engine())

