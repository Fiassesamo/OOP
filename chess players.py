class ChessPlayers:
    def __init__(self, name, surname, rating):
        self.name = name
        self.surname = surname
        self.rating = rating

    def __eq__(self, other):
        if isinstance(other, ChessPlayers):
            return (self.name == other.name and
                    self.surname == other.surname and
                    self.rating == other.rating)
        if isinstance(other, (int, str)):
            return self.name == other or self.surname == other or self.rating == other

        else:
            return 'We cannot do it'

    def __gt__(self, other):
        if isinstance(other, ChessPlayers):
            return self.rating > other.rating
        if isinstance(other, int):
            return self.rating > other
        else:
            return 'We cannot do it'

    def __lt__(self, other):
        if isinstance(other, ChessPlayers):
            return self.rating < other.rating
        if isinstance(other, int):
            return self.rating < other
        else:
            return 'We cannot do it'


magnus = ChessPlayers('Carlsen', 'Magnus', 2847)
ian = ChessPlayers('Ian', 'Nepomiachtchi', 2789)
print(magnus == 4000)
print(ian == 2789)
print(magnus == ian)
print(magnus > ian)
print(magnus < ian)
print(magnus < [1, 2])
