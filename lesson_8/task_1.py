class Data:
    def __init__(self, data):
        self.day, self.month, self.year = self.extract_data(data)

    @classmethod
    def extract_data(cls, data):
        try:
            day, month, year = map(int, data.split("-"))
        except ValueError as message:
            print(message)
            return 0, 1, 0
        else:
            if Data.check_data(day, month, year):
                return day, month, year
            else:
                print("Incorrect input data!")
                return 0, 1, 0

    @staticmethod
    def check_data(d, m, y):
        return all([0 <= d <= 31, 1 <= m <= 12, 0 < y <= 2022])


my_birthday = Data("28-01-1976")
print(my_birthday.day, my_birthday.month, my_birthday.year)
