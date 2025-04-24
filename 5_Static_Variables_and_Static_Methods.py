class MathUtils:
    @staticmethod
    def add(a: int, b: int) -> int:
        return (a + b)
    
if __name__ in "__main__" :
    sum_1 : MathUtils = MathUtils()
    print(sum_1.add(4,6))

    sum_2 : MathUtils = MathUtils()
    print(sum_2.add(72, 45))