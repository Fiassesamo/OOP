from datetime import datetime
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def date(self):
        eu_format = '%d/%m/%Y'
        date = f'{str(self.day)}/{str(self.month)}/{str(self.year)}'
        date_object = datetime.strptime(date, eu_format)
        self.date_obj = date_object.strftime("%Y/%m/%d")
        return self.date_obj

    def usa_date(self):
        usa_format = '%m/%d/%Y'
        date = f'{self.month}/{self.day}/{self.year}'
        date_object = datetime.strptime(date, usa_format)
        self.date_obj = date_object.strftime("%Y-%m-%d")
        return self.date_obj

Day1 = Date(5, 10, 2001)
Day1.date()
Day1.usa_date()
print(Day1.date(), Day1.usa_date())