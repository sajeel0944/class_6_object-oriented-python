from abc import ABC, abstractmethod
from typing import Union

class Shape(ABC):
    @abstractmethod
    def area():
        pass

 
class Rectangle(Shape):
    def __init__(self, width:  Union[float, int] , height:  Union[float, int] ):
        self.weigth : Union[float, int] = width
        self.height :  Union[float, int]  = height

    def area(slef) ->  Union[float, int] :
        return (slef.weigth * slef.height)
    
if __name__ in "__main__" :
    rect : Rectangle = Rectangle(32.3, 43)
    print(rect.area())





## use dataclass

from dataclasses import dataclass


class Shape_2(ABC):
    @abstractmethod
    def area():
        pass


@dataclass
class Rectangle_2(Shape_2):
    weigth : Union[float, int] 
    height :  Union[float, int] 

    def area(slef) ->  Union[float, int] :
        return (slef.weigth * slef.height)
    
if __name__ in "__main__" :
    rect_2 : Rectangle_2 = Rectangle_2(32.3, 43)
    print(rect_2.area())
