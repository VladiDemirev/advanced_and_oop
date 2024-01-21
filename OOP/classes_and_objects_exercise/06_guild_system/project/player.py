from typing import Dict


class Player:
    def __init__(self, player_name: str, hp: int, mp: int):
        self.player_name = player_name
        self.hp = hp
        self.mp = mp
        self.skills: Dict[str: int] = {}
        self.guild: str = "Unaffiliated"

    def add_skill(self, skill_name: str, mana_cost: int) -> str:
        # if skill_name not in self.skills:
        #     self.skills[skill_name] = mana_cost
        #
        #     return f"Skill {skill_name} added to the collection of the player {self.player_name}"
        #
        # return "Skill already added"

        if skill_name in self.skills:
            return "Skill already added"

        self.skills[skill_name] = mana_cost

        return f"Skill {skill_name} added to the collection of the player {self.player_name}"

    def player_info(self) -> str:
        # result = f"Name: {self.player_name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}\n"
        # skill_details = "\n".join([f"==={skill} - {mana}" for skill, mana in self.skills.items()])
        # result += skill_details
        #
        # return result

        skill_details = "\n".join([f"==={skill} - {mana}" for skill, mana in self.skills.items()])

        return f"Name: {self.player_name}\n" + \
               f"Guild: {self.guild}\n" + \
               f"HP: {self.hp}\n" + \
               f"MP: {self.mp}\n" + \
               f"{skill_details}"
