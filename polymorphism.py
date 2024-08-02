class Rectangle:
    def __init__(self,a ,b):
        self.a = a
        self.b = b



    def get_area(self):
        return self.a * self.b

    def __str__(self):
        return f'Rectangle {self.a}x{self.b}={self.get_area()}'

class Square:
    def __init__(self, a):
        self.a = a

    def __str__(self):
        return f'Square {self.a}x{self.a}={self.get_area()}'


    def get_area(self):
        return self.a**2


class Circe:
    def __init__(self, r):
        self.r = r

    def __str__(self):
        return f'Circe 3.14x{self.r}={self.get_area()}'

    def get_area(self):
        return 3.14 * self.r**2