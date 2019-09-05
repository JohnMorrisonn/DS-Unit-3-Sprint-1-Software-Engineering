class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    def add(self, number):
        self.r = self.r + number
        self.i = self.i + number

    def multiply(self, number):
        self.r = self.r * number
        self.i = self.i * number

    def divide(self, number):
        self.r = self.r / number
        self.i = self.i / number

    def sqrt(self):
        self.r = self.r ** 0.5
        self.i = self.i ** 0.5

x = Complex(3.0, -4.5)
x.add(5)
x.r, x.i
x.multiply(3)
x.r, x.i
x.divide(2)
x.r, x.i
x.sqrt()
x.r, x.i
