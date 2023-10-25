class Car:
    def __init__(self, name, mileage):
        self.name=name
        self.mileage=mileage
    def info(self):
        print(f"Машина марки {self.name} с пробегом {self.mileage}")
    @staticmethod
    def convert(miles):
        return miles*1.60934
    @classmethod
    def from_dict(cls, car_dict):
        name=car_dict.get('name', '')
        mileage=car_dict.get('mileage', 0)
        return cls(name, mileage)



car1 = Car("BMW", 10000)
car1.info()
miles = 50
kilometers = Car.convert(miles)
print(kilometers)

car_dict = {'name': 'Audi', 'mileage': 20000}
car2 = Car.from_dict(car_dict)
car2.info()