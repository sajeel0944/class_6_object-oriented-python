class A:
    def show(self) -> str:
        return ("This is class A")
    
class B(A):
    def show(self) -> str:
        return ("This is class B")
    
class C(A):
    def show(self) -> str:
        return ("This is class C")
    
    
class D(B, C):
    pass

if __name__ in "__main__" :
    d : D = D()
    print(d.show())
    print(D.__mro__)