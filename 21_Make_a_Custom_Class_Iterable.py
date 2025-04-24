class Countdown:
    def __init__(self, start: int):
        self.start : int= start
        self.current : int = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

if __name__ == "__main__":
    countdown : Countdown = Countdown(5)
    for num in countdown:
        print(num) 



## use dataclass


from dataclasses import dataclass
from typing import Iterator

@dataclass
class Countdown_2:
    start: int
    current: int = None  

    def __post_init__(self) -> None:
        self.current = self.start 
    
    def __iter__(self) -> Iterator[int]:
        return self
    
    def __next__(self) -> int:
        if self.current < 0:
            raise StopIteration
        value: int = self.current
        self.current -= 1
        return value

if __name__ == "__main__":
    countdown_2 : Countdown_2 = Countdown_2(5)
    for num in countdown_2:
        print(num)  