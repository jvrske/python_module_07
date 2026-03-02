from ex0.Card import Card
from ex2.Combatable import Combatable
from .Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, card_id: str, name: str, rating: int) -> None:
        self.card_id = card_id
        self._name = name
        self._last_result = None
        Rankable.__init__(self, rating=rating, wins=0, losses=0)

    def play(self, game_state):
        return super().play(game_state)

    def attack(self, target):
        return super().attack(target)

    def defend(self, incoming_damage):
        return super().defend(incoming_damage)

    def calculate_rating(self):
        if self._last_result == "win":
            self._rating += 16
        elif self._last_result == "loss":
            self._rating -= 16
        self._last_result = None
        return self._rating

    def update_wins(self, wins: int) -> None:
        self._wins += wins
        self._last_result = "win"

    def update_losses(self, losses: int) -> None:
        self._losses += losses
        self._last_result = "loss"

    def get_rank_info(self) -> dict:
        return {
            "id": self.card_id,
            "name": self._name,
            "rating": self._rating,
            "wins": self._wins,
            "losses": self._losses
        }

    def get_combat_stats(self):
        return super().get_combat_stats()

    def get_tournament_stats(self) -> dict:
        pass
