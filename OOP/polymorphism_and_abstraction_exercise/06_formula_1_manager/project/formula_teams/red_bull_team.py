from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):

    # def __init__(self, budget: int):
    #     super().__init__(budget)

    # def calculate_revenue_after_race(self, race_pos: int) -> str:
    #     expenses = 250_000
    #     # revenue = - expenses
    #
    #     sponsors = {
    #         "Oracle": {1: 1_500_000, 2: 800_000},
    #         "Honda": {8: 20_000, 10: 10_000},
    #     }

        # revenue = 0
        #
        # for s in sponsors.values():
        #     for position, prize in s.items():
        #         if race_pos <= position:
        #             revenue += prize
        #             break
        #
        # revenue -= expenses
        # self.budget += revenue
        # return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"

    @staticmethod
    def get_team_data():
        expenses = 250_000
        sponsors = {
            "Oracle": {1: 1_500_000, 2: 800_000},
            "Honda": {8: 20_000, 10: 10_000},
        }
        return expenses, sponsors
