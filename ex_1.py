class PowerTwo:
    def __init__(self, value):
        self.value = value
        self.index = 0
    def __iter__(self):
        return self

    def __next__(self):
        if self.index > self.value:
            raise StopIteration
            self.index = 0
        number = 2**self.index
        self.index+=1
        return number

for i in PowerTwo(4):
    print(i)


numbers = PowerTwo(2)
iterator = iter(numbers)
print((next(iterator)))
print((next(iterator)))
print((next(iterator)))
print((next(iterator)))
