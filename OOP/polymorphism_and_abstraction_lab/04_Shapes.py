from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        self.__radius = radius

    def calculate_area(self) -> float:
        return pi * self.__radius ** 2

    def calculate_perimeter(self) -> float:
        return 2 * pi * self.__radius


class Rectangle(Shape):
    def __init__(self, height: int, width: int):
        self.__height = height
        self.__width = width

    def calculate_area(self) -> int:
        return self.__height * self.__width

    def calculate_perimeter(self) -> int:
        return 2 * (self.__height + self.__width)


#  TEST CODE

circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())

rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())
