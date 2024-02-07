from abc import ABC, abstractmethod
from typing import List, Optional

from project.food import Food


class Animal(ABC):
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @property
    @abstractmethod
    def gained_weight(self) -> float:
        pass

    @property
    @abstractmethod
    def food_eaten(self) -> List[Food]:
        pass

    @property
    @abstractmethod
    def make_sound(self):
        pass

    def feed(self, food: "Food") -> Optional[str]:
        if type(food) not in self.food_eaten:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Bird(Animal, ABC):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
