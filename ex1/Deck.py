from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard
import random


class Deck():
    def __init__(self):
        self._deck = []

    def add_card(self, card: Card) -> None:
        self._deck.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self._deck:
            if card._name == card_name:
                self._deck.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        if len(self._deck) > 1:
            random.shuffle(self._deck)

    def draw_card(self) -> Card:
        return self._deck.pop(0)

    def get_deck_stats(self) -> dict:
        creature = 0
        spell = 0
        artifact = 0
        total_cost = 0
        for card in self._deck:
            total_cost += card._cost
        average = (round(total_cost / len(self._deck)))
        for card in self._deck:
            if isinstance(card, CreatureCard):
                creature += 1
            if isinstance(card, SpellCard):
                spell += 1
            if isinstance(card, ArtifactCard):
                artifact += 1
        return {
            "total_cards:": len(self._deck),
            "creatures:": creature,
            "spells": spell,
            "artifacts": artifact,
            "avg_cost": average
        }
