from typing import List

from project.animals.animal import Bird
from project.food import Food, Meat, Vegetable, Fruit


class Owl(Bird):

    @property
    def gained_weight(self) -> float:
        return 0.25

    @property
    def food_eaten(self) -> List:
        return [Meat]

    @property
    def make_sound(self) -> str:
        return "Hoot Hoot"


class Hen(Bird):

    @property
    def gained_weight(self) -> float:
        return 0.35

    @property
    def food_eaten(self) -> List:
        return [Meat, Vegetable, Fruit]

    @property
    def make_sound(self) -> str:
        return "Cluck"
