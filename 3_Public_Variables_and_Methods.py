class Car:
    def __init__(self):
        self.brand : str = "Toyota"
 
    def start(self) -> str:
        return f"Engine started!"
    
car : Car = Car()

if __name__ in "__main__" :
    print(car.brand)
    print(car.start())




## use dataclass

class Car_1():
    brand : str = "Toyota"

    def start(self) -> str:
        return f"Engine started!"
    
car_1 : Car = Car()

if __name__ in "__main__" :
    print(car_1.brand)
    print(car_1.start())
