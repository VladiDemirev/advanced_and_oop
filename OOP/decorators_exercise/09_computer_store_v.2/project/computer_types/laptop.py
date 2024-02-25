from project.computer_types.computer import Computer
from math import log2


class Laptop(Computer):

    def valid_ram(self):
        return 64

    def valid_processor(self):
        return {
            "AMD Ryzen 9 5950X": 900,
            "Intel Core i9-11900H": 1050,
            "Apple M1 Pro": 1200,
        }

    def __str__(self):
        return "laptop"
