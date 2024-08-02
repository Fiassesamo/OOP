class Money:
    def __init__(self, dolar, cents):
        self.total_cents = 100*dolar + cents
        self.dolar = dolar
        self.cents = cents

    @property
    def dollars(self):
        return self.dolar

    @dollars.setter
    def dollars(self, new_dollars):
        if isinstance(new_dollars, (int, float)) and new_dollars >= 0:
            self.dolar = new_dollars
            self.total_cents = 100*self.dolar + self.cents
        else:
            raise ValueError('Error dollars')

    @property
    def my_cents(self):
        return self.cents

    @my_cents.setter
    def my_cents(self, new_cents):
        if isinstance(new_cents, (int, float)) and new_cents >= 0:
            if new_cents >=100:
                dollar_in_cents = int(new_cents / 100)
                self.dolar = dollar_in_cents + self.dolar
                self.cents = new_cents - (dollar_in_cents * 100)
        else:
            raise ValueError('Error Cents')

    def __str__(self):
        return f'Your money {self.dolar} dollars {self.cents} cents'

Bill = Money(101, 99)
print(Bill)
print(Bill.dollars, Bill.my_cents)
print(Bill.total_cents)
Bill.dollars = 660
print(Bill.dollars)
Bill.my_cents = 501
print(Bill.dollars, Bill.my_cents)