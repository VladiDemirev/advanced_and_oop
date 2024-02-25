from project.computer_types.computer import Computer
from math import log2


class Laptop(Computer):

    def configure_computer(self, processor: str, ram: int):
        available_processors = {
            "AMD Ryzen 9 5950X": 900,
            "Intel Core i9-11900H": 1050,
            "Apple M1 Pro": 1200,
        }
        max_ram = 64
        # valid_ram_sizes = [2 ** n for n in range(1, 7)]
        valid_ram_sizes = [2 ** n for n in range(int(log2(max_ram) + 1))]

        if processor not in available_processors:
            raise ValueError(f"{processor} is not compatible with laptop {self.manufacturer} {self.model}!")

        if ram not in valid_ram_sizes:
            raise ValueError(f"{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!")

        processor_price = available_processors[processor]
        ram_price = int(log2(ram)) * 100
        self.processor = processor
        self.ram = ram
        self.price = processor_price + ram_price
        # self.price = available_processors[processor] + int(log(ram, 2)) * 100

        return f"Created {self.__repr__()} for {self.price}$."
