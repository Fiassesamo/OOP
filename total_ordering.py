class Quadrilaltera:
    def __init__(self, width, height=None):
        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height

    def __str__(self):
        if self.height == self.height:
            return f'Square size {self.width} {self.height}'
        else:
            return f'Quadrilaltera size {self.width} {self.height}'

    def __bool__(self):
        return  self.width == self.height


q1 = Quadrilaltera(10)
print(q1)
print(bool(q1))
q2 = Quadrilaltera(3, 5)
print(q2)
print(bool(q2))