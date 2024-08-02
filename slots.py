class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y



class PointsSlots:

    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y



a = Point(3, 4)
print(a.__sizeof__())
