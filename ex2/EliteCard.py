from ex0.Card import Card
from ex0.Card import Rarity
from .Combatable import Combatable
from .Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, combat_type: str, damage: int,
                 health: int, defense: int, mana: int):
        super().__init__(name, cost, Rarity.LEGENDARY.value)
        self._name = name
        self._cost = cost
        self._combat_type = combat_type
        self._damage = damage
        self._health = health
        self._defense = defense
        self._mana = mana

    def play(self, game_state: dict) -> dict:
        pass

    def attack(self, target: str) -> dict:
        return {
            "attacker": self._name,
            "target": target._name,
            "damage": self._damage,
            "combat_type": self._combat_type
        }

    def defend(self, incoming_damage: int) -> dict:
        damage = abs(self._defense - incoming_damage)
        self._health -= damage
        alive = True
        if self._health <= 0:
            alive = False
        return {
            "defender": self._name,
            "damage_taken": damage,
            "damage_blocked": self._defense,
            "still_alive": alive
        }

    def channel_mana(self, amount):
        self._mana += amount
        return {'channeled': amount,
                'total_mana': self._mana}

    def get_combat_stats(self):
        return {'health': self._health, 'mana': self._mana}

    def get_magic_stats(self):
        return {'mana_remaining': self._mana}

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        self._mana -= self._cost
        return {
            "caster": self._name,
            "spell": spell_name,
            "targets": [t._name for t in targets],
            "mana_used": self._cost
        }
