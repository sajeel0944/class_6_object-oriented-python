def add_greeting(cls):
    def greet(self) -> str:
        return "Hello from Decorator!"
    
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self, name: str):
        self.name = name


if __name__ in "__main__":
    person = Person("sajeel")
    print(person.greet())