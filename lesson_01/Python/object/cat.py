class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")


# 定义一个燃油车的类
class GasCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.gas_tank_size = 75

    def describe_gas_tank(self):
        print(f"This car has a {self.gas_tank_size}-kWh gas tank.")

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")


my_tesla = ElectricCar('tesla', 'model s', 2021)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

# 丰田燃油车的对象
my_toyota = GasCar('toyota', 'camry', 2021)
print(my_toyota.get_descriptive_name())
my_toyota.describe_gas_tank()

# 遍历一个汽车列表
cars = [my_tesla, my_toyota]
for car in cars:
    print(car.get_descriptive_name())
    car.fill_gas_tank()

# 面向对象编程

# 面向流程编程

def main():
    pass

