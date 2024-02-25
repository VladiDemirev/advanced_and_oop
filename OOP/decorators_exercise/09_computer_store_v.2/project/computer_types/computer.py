from abc import ABC, abstractmethod
from math import log2
from typing import Optional


class Computer(ABC):
    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor: Optional[str] = None
        self.ram: Optional[int] = None
        self.price: int = 0

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        # if not value or value.isspace():
        if value.strip() == "":
            raise ValueError("Manufacturer name cannot be empty.")
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        # if not value or value.isspace():
        if value.strip() == "":
            raise ValueError("Model name cannot be empty.")
        self.__model = value

    @property
    @abstractmethod
    def valid_ram(self):
        pass

    @property
    @abstractmethod
    def valid_processor(self):
        pass

    def configure_computer(self, processor: str, ram: int):
        valid_processors = self.valid_processor()
        max_ram = self.valid_ram()
        valid_ram = [2 ** n for n in range(int(log2(max_ram) + 1))]
        if processor not in valid_processors:
            raise ValueError(f"{processor} is not compatible with {self.__str__()} {self.manufacturer} {self.model}!")

        if ram not in valid_ram:
            raise ValueError(f"{ram}GB RAM is not compatible with {self.__str__()} {self.manufacturer} {self.model}!")

        processor_price = valid_processors[processor]
        ram_price = int(log2(ram)) * 100
        self.processor = processor
        self.ram = ram
        self.price = processor_price + ram_price

        return f"Created {self.__repr__()} for {self.price}$."

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"
