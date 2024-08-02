# value = []
# value.extend([None] * 20)
# print(value)



class Building:
    def __init__(self, floors):
        self.value = []
        self.value.extend([None] * floors)

    def __str__(self):
        return f'{self.value}'


    def __getitem__(self, item):
        if 0 <= item < len(self.value):
            return self.value[item]


    def __setitem__(self, key, value):
        if 0 <= key < len(self.value):
            if self.value[key] is None:
                self.value[key] = value
            else:
                raise ValueError(f'This floor is busy {self.value[key]}')
        else:
            return 'Error'


    def __delitem__(self, key):
        if  0 <= key < len(self.value):
            self.value[key] = None


a = Building(22)
a[0] = 'Reception'
a[1] = 'Oscorp Industries'
a[2] = 'Stark Industries'
print(a[1])
print(a[2])
del a[1]
print(a[1])