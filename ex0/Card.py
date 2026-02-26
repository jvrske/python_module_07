from abc import ABC, abstractmethod
from enum import Enum


class Rarity(Enum):
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    LEGENDARY = "Legendary"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self._name = name
        self._cost = cost
        self._rarity = self._valid_rarity(rarity)

    @abstractmethod
    def play(self, game_state: dict) -> bool:
        pass

    def _valid_rarity(self, rarity: str) -> str:
        rarity_stand = rarity.lower()
        for i in Rarity:
            if i.value.lower() == rarity_stand:
                return i.value
        raise ValueError

    def get_card_info(self) -> dict:
        card_info = {
            "name": self._name,
            "cost": self._cost,
            "rarity": self._rarity
        }
        return card_info

    def is_playable(self, available_mana: int) -> bool:
        if available_mana >= self._cost:
            return True
        return False
