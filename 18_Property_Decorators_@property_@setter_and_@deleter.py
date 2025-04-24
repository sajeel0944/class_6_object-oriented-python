class Product:
    def __init__(self, name: str, price: float):
        self.name : str = name
        self._price : float = price

    @property
    def price(self) -> float:
        return self._price
    
    @price.setter
    def price(self, value: float) -> None:
        if value == 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    @price.deleter
    def price(self) -> None:
        del self._price


if __name__ in "__main__":
    products : Product = Product("Laptop", 35.32)
    print(products.price)

    products.price = 32.43
    print(products.price)

    del products.price

    try:
        print(products.price)  
    except AttributeError as e:
        print(f"Error: {e}")  




## use dataclass


from dataclasses import dataclass

@dataclass
class Product:
    name : str
    price : float

    @property
    def price(self) -> float:
        return self._price
    
    @price.setter
    def price(self, value: float) -> None:
        if value == 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    @price.deleter
    def price(self) -> None:
        del self._price

 
if __name__ in "__main__":
    products : Product = Product("Laptop", 35.32)
    print(products.price)

    products.price = 32.43
    print(products.price)

    del products.price

    try:
        print(products.price)  
    except AttributeError as e:
        print(f"Error: {e}")  