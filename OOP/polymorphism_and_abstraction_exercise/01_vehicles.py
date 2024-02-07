from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance: int):
        pass

    @abstractmethod
    def refuel(self, fuel: int):
        pass


class Car(Vehicle):
    EXTRA_CONSUMPTION = 0.9

    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance: int) -> None:
        used_fuel = (self.fuel_consumption + Car.EXTRA_CONSUMPTION) * distance
        if used_fuel <= self.fuel_quantity:
            self.fuel_quantity -= used_fuel

    def refuel(self, fuel: int) -> None:
        self.fuel_quantity += fuel


class Truck(Vehicle):
    EXTRA_CONSUMPTION = 1.6
    LOST_FUEL = 0.95

    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance: int) -> None:
        used_fuel = (self.fuel_consumption + Truck.EXTRA_CONSUMPTION) * distance
        if used_fuel <= self.fuel_quantity:
            self.fuel_quantity -= used_fuel

    def refuel(self, fuel: int) -> None:
        self.fuel_quantity += fuel * Truck.LOST_FUEL


#  TEST CODE

car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
