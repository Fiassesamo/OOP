
class Vector:
    def __init__(self, *args):
        self.value = sorted(args)


    def __str__(self):
        if self.value:
            return f'Vector{self.value}'
        else:
            return f'Empty vector'


    def __add__(self, other):
        if isinstance(other, (float, int)):
            new_vector = [i + other for i in self.value]
            return Vector(*new_vector)
        if isinstance(other, Vector):
            if len(other.value) == len(self.value):
                new_vector = [self.value[i] + other.value[i] for i in range(len(self.value))]
                return Vector(*new_vector)
            else:
                return f'vectors have Different length'
        return f'we can\'n add to vector string type or another non compatible data type'

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            new_vector = [i * other for i in self.value]
            return Vector(*new_vector)
        if isinstance(other, Vector):
            if len(other.value) == len(self.value):
                new_vector = [self.value[i] * other.value[i] for i in range(len(self.value))]
                return Vector(*new_vector)
            else:
                return f'vectors have Different length'
        raise NotImplemented(f'we can\'n multiple to vector string type or another non compatible data type')



v1 = Vector(1, 2, 3)
print(v1)
v2 = Vector(3, 4, 5)
print(v2)
v3 = v1 + v2
print(v3)
v4 = v3 + 5
print(v4)
v5 = v1 * 2
print(v5 + 'hi')
print(v3, v4)
