from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):

    # def __init__(self, budget: int):
    #     super().__init__(budget)

    # def calculate_revenue_after_race(self, race_pos: int) -> str:
    #     expenses = 200_000
    #     # revenue = - expenses
    #
    #     sponsors = {
    #         "Petronas": {1: 1_000_000, 3: 500_000},
    #         "TeamViewer": {5: 100_000, 7: 50_000},
    #     }
    #
    #     # revenue = 0
    #     #
    #     # for s in sponsors.values():
    #     #     for position, prize in s.items():
    #     #         if race_pos <= position:
    #     #             revenue += prize
    #     #             break
    #     #
    #     # revenue -= expenses
    #     # self.budget += revenue
    #     # return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"

    @staticmethod
    def get_team_data():
        expenses = 200_000
        sponsors = {
                "Petronas": {1: 1_000_000, 3: 500_000},
                "TeamViewer": {5: 100_000, 7: 50_000},
            }
        return expenses, sponsors
