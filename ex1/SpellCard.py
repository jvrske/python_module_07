from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        self._name = name
        self._cost = cost
        self.rarity = rarity
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        game_state = {"card_played": self._name, "mana_used": self._cost,
                      "effect": "Deal 3 damage to target"}
        return game_state

    def resolve_effect(self, targets: list) -> dict:
        pass
