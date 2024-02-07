from typing import List

from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):

    @property
    def gained_weight(self) -> float:
        return 0.10

    @property
    def food_eaten(self) -> List:
        return [Vegetable, Fruit]

    @property
    def make_sound(self) -> str:
        return "Squek"


class Dog(Mammal):

    @property
    def gained_weight(self) -> float:
        return 0.40

    @property
    def food_eaten(self) -> List:
        return [Meat]

    @property
    def make_sound(self) -> str:
        return "Cluck"


class Cat(Mammal):

    @property
    def gained_weight(self) -> float:
        return 0.30

    @property
    def food_eaten(self) -> List:
        return [Meat, Vegetable]

    @property
    def make_sound(self) -> str:
        return "Meow"


class Tiger(Mammal):

    @property
    def gained_weight(self) -> float:
        return 1.00

    @property
    def food_eaten(self) -> List:
        return [Meat]

    @property
    def make_sound(self) -> str:
        return "ROAR!!!"
