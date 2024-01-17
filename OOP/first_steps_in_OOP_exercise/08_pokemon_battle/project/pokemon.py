class Pokemon:
    def __init__(self, pokemon_name: str, pokemon_health: int):
        self.pokemon_name = pokemon_name
        self.pokemon_health = pokemon_health

    def pokemon_details(self) -> str:
        return f"{self.pokemon_name} with health {self.pokemon_health}"
