class Counter:
    count : int = 0
 
    def __init__(self):
        Counter.count += 1

    @classmethod
    def display(cls) -> str:
        return (f"Total objects created: {cls.count}")

obj_1 : Counter = Counter()
obj_2 : Counter = Counter()
obj_3 : Counter = Counter()
obj_4 : Counter = Counter()

if __name__ in "__main__" :
    print(obj_4.display())


