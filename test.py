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
    
    def full_div(self, a, b):
        return a // b
    
    def plusplus(self, a):
        return a + 1
    def ack(self, a, b):
        if a == 0:
            return b + 1
        elif b == 0:
            return self.ack(a - 1, 1)
        else:
            return self.ack(a - 1, self.ack(a, b - 1))

if __name__ == '__main__':
    calc = CalcClass()
    print(calc.add(1, 2))    
