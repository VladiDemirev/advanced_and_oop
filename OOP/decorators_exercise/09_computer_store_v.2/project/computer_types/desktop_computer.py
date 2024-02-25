from project.computer_types.computer import Computer
from math import log2


class DesktopComputer(Computer):

    def valid_ram(self):
        return 128

    def valid_processor(self):
        return {
            "AMD Ryzen 7 5700G": 500,
            "Intel Core i5-12600K": 600,
            "Apple M1 Max": 1800,
        }

    def __str__(self):
        return "desktop computer"
