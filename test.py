class CalcClass():
    def __init__(self) -> None:
        pass

    def add(self, a, b):
        return a + b
    
    def sub(self, a, b):
        return a - b
    
    def mul(self, a, b):
        return a * b
    
    def div(self, a, b):
        return a / b
    
    def mod(self, a, b):
        return a % b
    
    def pow(self, a, b):
        return a ** b

if __name__ == '__main__':
    calc = CalcClass()
    print(calc.add(1, 2))    
