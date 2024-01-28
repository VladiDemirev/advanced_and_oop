from typing import Dict, Optional, Union

from project.dough import Dough
from project.topping import Topping


class Pizza:
    def __init__(self, name: str, dough: Dough, max_number_of_toppings: int):
        self.name = name
        self.dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings: Dict[str, int] = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str) -> Union[str, None]:
        if value == "":
            raise ValueError("The name cannot be an empty string")
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value: Dough) -> Optional[str]:
        if value is None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = value

    @property
    def max_number_of_toppings(self):
        return self.__max_number_of_toppings

    @max_number_of_toppings.setter
    def max_number_of_toppings(self, value: int) -> Optional[str]:
        if value <= 0:
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")
        self.__max_number_of_toppings = value

    def add_topping(self, topping: Topping) -> Optional[str]:
        if len(self.toppings) == self.max_number_of_toppings:
            raise ValueError("Not enough space for another topping")
        elif topping.topping_type not in self.toppings:
            self.toppings[topping.topping_type] = topping.weight
        else:
            self.toppings[topping.topping_type] += topping.weight

    def calculate_total_weight(self) -> int:
        # toppings_weight = sum([v for v in self.toppings.values()])
        toppings_weight = sum(self.toppings.values())
        dough_weight = self.dough.weight
        return dough_weight + toppings_weight
