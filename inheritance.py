class NewInt(int):

    def repeat(self, value=2):
        return int(str(self) * value)

    def to_bin(self):
        return int(bin(self)[2:])




a = NewInt(9)
print(a.repeat())
d = NewInt(a + 5)
print(d.repeat(3))
b = NewInt(NewInt(7) * NewInt(5))
print(b.to_bin())
print(NewInt())