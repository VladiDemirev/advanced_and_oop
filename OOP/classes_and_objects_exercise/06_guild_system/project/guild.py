from typing import List
from project.player import Player


class Guild:
    def __init__(self, guild_name: str):
        self.guild_name = guild_name
        self.players: List[Player] = []

    def assign_player(self, player: Player) -> str:
        # if player in self.players:
        #     if player.guild != self.guild_name:
        #         return f"Player {player.player_name} is in another guild."
        #
        #     return f"Player {player.player_name} is already in the guild."
        #
        # self.players.append(player)
        # player.guild = self.guild_name
        #
        # return f"Welcome player {player.player_name} to the guild {self.guild_name}"

        # if player in self.players:
        if player.guild == self.guild_name:

            return f"Player {player.player_name} is already in the guild."

        if player.guild != "Unaffiliated":

            return f"Player {player.player_name} is in another guild."

        self.players.append(player)
        player.guild = self.guild_name

        return f"Welcome player {player.player_name} to the guild {self.guild_name}"

    def kick_player(self, player_name: str) -> str:
        try:
            player = next(filter(lambda x: x.player_name == player_name, self.players))
        except StopIteration:
            return f"Player {player_name} is not in the guild."

        self.players.remove(player)
        player.guild = "Unaffiliated"

        return f"Player {player_name} has been removed from the guild."

    def guild_info(self) -> str:
        player_info = "\n".join([p.player_info() for p in self.players])
        return f"Guild: {self.guild_name}\n" + \
               f"{player_info}"
