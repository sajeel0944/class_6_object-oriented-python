class Multiplier:
    def __init__(self, factor: float):
        self.factor : float = factor

    def __call__(self, value: float) -> float:
        return value * self.factor
    

if __name__ in "__main__":
    user : Multiplier = Multiplier(5)
    print(user(2))



##  use dataclass

from dataclasses import dataclass

@dataclass
class Multiplier:
    factor : float

    def __call__(self, value: float) -> float:
        return value * self.factor
     

if __name__ in "__main__":
    user : Multiplier = Multiplier(5)
    print(user(2))
