import random
from enum import Enum
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from .CardFactory import CardFactory


class FantasyType(Enum):
    CREATURE = "creature"
    SPELL = "spell"
    ARTIFACT = "artifact"


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self._creatures = {
            "dragon": {"name": "Fire Dragon", "cost": 5, "rarity": "Legendary",
                       "attack": 7, "health": 5},
            "goblin": {"name": "Goblin Warrior", "cost": 2, "rarity": "Common",
                       "attack": 2, "health": 1}
        }
        self._spells = {
            "lightning_bolt": {"name": "Lightning Bolt", "cost": 3, "rarity":
                               "Common", "effect_type": "damage"},
            "fireball": {"name": "Fireball", "cost": 4, "rarity": "Uncommon",
                         "effect_type": "damage"}
        }
        self._artifacts = {
            "mana_ring": {"name": "Mana Ring", "cost": 2, "rarity": "Common",
                          "durability": 3, "effect": "Gain 1 mana per turn"}
        }

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str) and name_or_power in self._creatures:
            data = self._creatures[name_or_power]
            return CreatureCard(data["name"], data["cost"], data["rarity"],
                                data["attack"], data["health"])

        if name_or_power is None:
            key = random.choice(list(self._creatures.keys()))
            data = self._creatures[key]
            return CreatureCard(data["name"], data["cost"], data["rarity"],
                                data["attack"], data["health"])

        if isinstance(name_or_power, int):
            key = random.choice(list(self._creatures.keys()))
            data = self._creatures[key]
            return CreatureCard(data["name"], data["cost"], data["rarity"],
                                data["attack"], data["health"])

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str) and name_or_power in self._spells:
            data = self._spells[name_or_power]
            return SpellCard(data["name"], data["cost"], data["rarity"],
                             data["effect_type"])

    def create_artifact(self, name_or_power=None):
        if isinstance(name_or_power, str) and name_or_power in self._artifacts:
            data = self._artifacts[name_or_power]
            return ArtifactCard(data["name"], data["cost"], data["rarity"],
                                data["durability"], data["effect"])

    def create_themed_deck(self, size):
        return super().create_themed_deck(size)

    def get_supported_types(self):
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"]
        }
