from datetime import datetime

from engine_factory import Engine


class Key:

    key = 1000000

    def __init__(self):
        Key.key += 1

    @classmethod
    def generate_key(cls):
        return cls.key


class Car:

    def __init__(self, car_type, model, color, year, engine):
        self.car_type = car_type
        self.model = model
        self.color = color
        self.year = year
        self.win_code = self._generate_win_code()
        self.engine = engine

    def _generate_win_code(self):
        today = datetime.now()
        month = today.strftime('%m')
        key = Key()
        self.win_code = (self.car_type[0] + "-" + self.color[0] + "-"
                         + str(self.year) + "-" + str(month) + "-"
                         + str(key.generate_key()))
        return self.win_code

    def __str__(self):
        return f"\nmodel: {self.car_type}, win code: {self.win_code}"

    @staticmethod
    def determine_age_of_car(car_year):
        today = datetime.now()
        year_now = today.strftime('%Y')
        return int(year_now) - car_year


engine_1 = Engine("Sharan 2000-2010", 16, "longitudinal arrangement",
                  1000, "petrol")
engine_2 = Engine("Sharan 2000-2010", 16, "longitudinal arrangement",
                  10000, "petrol")
car_1 = Car("sedan", "bmw", "black", 2020, engine_1)
car_2 = Car("universal", "audi", "red", 2010, engine_2)
print(car_2)
print(car_1.determine_age_of_car(car_1.year))
