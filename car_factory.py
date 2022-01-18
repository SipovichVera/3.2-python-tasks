from datetime import datetime

# from engine_factory import Engine

class Key:

    key = 1000000

    def __init__(self):
        self.__class__.key += 1

    # @classmethod
    def generate_key(cls):
        return cls.key

class Car:

    def __init__(self, car_type, model, color):
        self.car_type = car_type
        self.model = model
        self.color = color
        self.win_code = self._generate_win_code()
        # self.engine = Engine()

    def _generate_win_code(self):
        today = datetime.now()
        year = today.strftime('%Y')
        month = today.strftime('%m')
        key = Key()
        self.win_code = self.car_type[0] + "-" + self.color[0] + "-" + str(year) + "-" + str(month) + "-" + str(key.generate_key())
        return self.win_code

    def __str__(self):
        return f"model: {self.car_type}, win code: {self.win_code}"


car_1 = Car("sedan", "bmw", "black")
car_2 = Car("universal", "audi", "red")
print(car_2)

