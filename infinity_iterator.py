class InfinityIterator:
    def __init__(self):
        self.iterator = 0


    def __iter__(self):
        return self


    def __next__(self):
        self.new_iter = self.iterator
        self.iterator +=10
        return self.new_iter


test = InfinityIterator()
for i in range(15):
    print(next(test))

print(next(test))