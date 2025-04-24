class Dog:
    def __init__(self, name: str, breed: str):
        self.name : str = name
        self.breed : str = breed

    def bark(self) -> str:
        return (f"Dog Name: {self.name}, Dog Breed {self.breed}")

if __name__ in "__main__" :
    dog : Dog = Dog("Buddy", "Golden Retriever")
    print(dog.bark())     

 


##  use dataclass

from dataclasses import dataclass

@dataclass
class Dog_2:
    name : str
    breed : str

    def bark(self) -> str:
        return (f"Dog Name: {self.name}, Dog Breed {self.breed}")

if __name__ in "__main__" :
    dog : Dog = Dog("Buddy", "Golden Retriever")
    print(dog.bark())     