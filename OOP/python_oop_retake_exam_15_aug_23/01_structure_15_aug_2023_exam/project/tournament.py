from typing import List

from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        is_valid_name = all([char.isalnum() for char in value])
        if not is_valid_name:
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str) -> str:
        valid_equipment = {"KneePad": KneePad, "ElbowPad": ElbowPad}
        if equipment_type not in valid_equipment:
            raise Exception("Invalid equipment type!")
        self.equipment.append(valid_equipment[equipment_type]())
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int) -> str:
        valid_teams = {"IndoorTeam": IndoorTeam, "OutdoorTeam": OutdoorTeam}
        if team_type not in valid_teams:
            raise Exception("Invalid team type!")
        if self.capacity == len(self.teams):
            return "Not enough tournament capacity."
        self.teams.append(valid_teams[team_type](team_name, country, advantage))
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str) -> str:
        equipment = [e for e in self.equipment if e.__class__.__name__ == equipment_type][-1]
        team = next((t for t in self.teams if t.name == team_name), None)
        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")
        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str) -> str:
        team = next((t for t in self.teams if t.name == team_name), None)
        if not team:
            raise Exception("No such team!")
        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")
        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str) -> str:
        equipment = [e for e in self.equipment if e.__class__.__name__ == equipment_type]
        for e in equipment:
            e.increase_price()
        return f"Successfully changed {len(equipment)}pcs of equipment."

    def play(self, team_name1: str, team_name2: str) -> str:
        team1 = next((t for t in self.teams if t.name == team_name1), None)
        team2 = next((t for t in self.teams if t.name == team_name2), None)
        if team_name1.__class__.__name__ != team_name2.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")
        total_protection_team1 = sum(e.protection for e in team1.equipment)
        team1_stats = team1.advantage + total_protection_team1
        total_protection_team2 = sum(e.protection for e in team2.equipment)
        team2_stats = team2.advantage + total_protection_team2
        if team1_stats == team2_stats:
            return "No winner in this game."
        winner = team1 if team1_stats > team2_stats else team2
        winner.win()
        return f"The winner is {winner.name}."

    def get_statistics(self) -> str:
        teams = sorted(self.teams, key=lambda t: -t.wins)
        result = f"Tournament: {self.name}\n" \
                 f"Number of Teams: {len(self.teams)}\n" \
                 "Teams:\n"
        team_data = "\n".join([t.get_statistics() for t in teams])
        return result + team_data


        # result = f"Tournament: {self.name}\n"\
        #          f"Number of Teams: {len(self.teams)}\n"\
        #          "Teams:\n"
        # team_data = "\n".join(t.get_statistics() for t in self.teams)
        # return result + team_data
