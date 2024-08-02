class Initialization:
    def __init__(self, caption, food:list):
        self.food = food
        if isinstance(caption, int):
            self.caption = caption
        else:
            print(f'Peoples are int number')



class Vegetarians(Initialization):
    def __init__(self, caption, food):
        super().__init__(caption, food)

    def __str__(self):
        return f'{self.caption} people don\'t eat meat they are Vegetarians and they eat {self.food}'

class MeatEater(Initialization):
    def __init__(self, caption, food):
        super().__init__(caption, food)

    def __str__(self):
        return f'{self.caption} are meat eater they eat {self.food}'



class SweetTooth(Initialization):
    def __init__(self, caption, food):
        super().__init__(caption, food)

    def __str__(self):
        return f'{self.caption} SweetTooth eater they eat food like {self.food}'

    def __eq__(self, other):
        if isinstance(other, (int, MeatEater, Vegetarians)):
            return (isinstance(other, int) and other == self.caption) or (
                    isinstance(other, (MeatEater, Vegetarians)) and other.caption == self.caption)
        else:
            return f'Can\'t do this operation'


    def __lt__(self, other):
        if isinstance(other, (int, MeatEater, Vegetarians)):
            return (isinstance(other, int) and other > self.caption) or (
                    isinstance(other, (MeatEater, Vegetarians)) and other.caption > self.caption)
        else:
            return f'Can\'t do this operation'

    def __gt__(self, other):
        if isinstance(other, (int, MeatEater, Vegetarians)):
            return (isinstance(other, int) and other < self.caption) or (
                        isinstance(other, (MeatEater, Vegetarians)) and other.caption < self.caption)
        else:
            return f'Can\'t do this operation'

v_first = Vegetarians(10000, ['O', 'O', 'F'])
print(v_first)
v_second = Vegetarians([23], ['None'])
m_first=MeatEater(15000, ['Chiken', 'Fish'])
print(m_first)
s_first = SweetTooth(30000, ['Icecream', 'Chips', 'Chocolate'])
print(s_first)
print(s_first > v_first)
print(30000 == s_first)
print(s_first == 25000)
print(100000 < s_first)
print(100 < s_first)