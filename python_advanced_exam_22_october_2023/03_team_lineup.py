def team_lineup(*args):
    players_collection = {}
    for player_name, country in args:
        if country not in players_collection:
            players_collection[country] = []
        players_collection[country].append(player_name)

    sorted_collection = sorted(players_collection.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    result = ""

    for country, players in sorted_collection:
        result += f"{country}:\n"
        for player in players:
            result += f"  -{player}\n"

    return result.strip()

print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))

print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))

print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))
