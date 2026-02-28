from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, durability: int,
                 effect: str) -> None:
        self._name = name
        self._cost = cost
        self.rarity = rarity
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        game_state = {"card_played": self._name, "mana_used": self._cost,
                      "effect": "Permanent: +1 mana per turn"}
        return game_state

    def activate_ability(self) -> dict:
        pass
