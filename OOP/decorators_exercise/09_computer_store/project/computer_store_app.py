from typing import List
from project.computer_types.computer import Computer
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    def __init__(self):
        self.warehouse: List[Computer] = []
        self.profits: int = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int) -> str:
        valid_computers = {"Desktop Computer": DesktopComputer, "Laptop": Laptop}

        if type_computer not in valid_computers:
            raise ValueError(f"{type_computer} is not a valid type computer!")
        computer = valid_computers[type_computer](manufacturer, model)
        result = computer.configure_computer(processor, ram)
        self.warehouse.append(computer)
        return result

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int) -> str:
        computer = next((c for c in self.warehouse if
                         c.price <= client_budget and
                         c.processor == wanted_processor and
                         c.ram >= wanted_ram), None)
        if not computer:
            raise Exception("Sorry, we don't have a computer for you.")

        self.profits += (client_budget - computer.price)
        self.warehouse.remove(computer)
        return f"{computer} sold for {client_budget}$."
