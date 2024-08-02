class Wallet:
    def __init__(self, currency:str, balance):
        if len(currency) == 3 and currency == currency.isupper():
            self.currency = currency
        else:
            raise
        self.balance = balance