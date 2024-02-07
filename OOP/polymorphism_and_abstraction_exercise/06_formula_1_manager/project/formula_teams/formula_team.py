from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    # BUDGET = 1_000_000

    def __init__(self, budget: int):
        self.budget = budget

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        # if value < FormulaTeam.BUDGET:
        if value < 1_000_000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budget = value

    @staticmethod
    @abstractmethod
    def get_team_data():
        pass

    def calculate_revenue_after_race(self, race_pos: int):
        expenses, sponsors = self.get_team_data()

        revenue = 0
        for s in sponsors.values():
            for position, prize in s.items():
                if race_pos <= position:
                    revenue += prize
                    break

        revenue -= expenses
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
