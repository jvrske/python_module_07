from .Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self._attack = self.valid_attack(attack)
        self._health = self.valid_health(health)

    def valid_attack(self, attack: int) -> int:
        if not isinstance(attack, int) or attack <= 0:
            raise ValueError("attack must be a positive integer")
        return attack

    def valid_health(self, health: int) -> int:
        if not isinstance(health, int) or health <= 0:
            raise ValueError("health must be a positive integer")
        return health

    def play(self, game_state: dict) -> dict:
        available_mana = game_state.get("mana")
        if not self.is_playable(available_mana):
            return {"error", "Not enough mana!"}
        game_state["mana"] = available_mana - self._cost

        return {
            "card_played": self._name,
            "mana_used": self._cost,
            "effect": "Creature summoned to battlefield"
        }

    def attack_target(self, target: str) -> dict:
        return {
            "attacker": self._name,
            "target": str(target),
            "damage_dealt": self._attack,
            "combat_resolved": True
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update({
            "type": "Creature",
            "attack": self._attack,
            "health": self._health
        })
        return info
