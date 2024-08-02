class Mark:
    def __init__(self, value):
        self.value = value
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        print('call next marks')
        if self.index >= len((self.value)):
            raise StopIteration
            self.index = 0
        letter = self.value[self.index]
        self.index +=1
        return letter


class Student:
    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks


    def __iter__(self):
        print("call iter")
        self.index = 0
        return iter(self.marks)

    def __next__(self):
        if self.index >= len((self.surname)):
            raise StopIteration
            self.index = 0
        letter = self.surname[self.index]
        self.index +=1
        return letter
m = Mark([3,4,5,6,3])
igor = Student('Igor', 'Nikolaew', m)

for i in igor:
    print(i)