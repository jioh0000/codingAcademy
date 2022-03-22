class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        print(self.a+self.b)
    def minus(self):
        print(self.a-self.b)

Calculator.add(2,10)
Calculator.minus(42,10)