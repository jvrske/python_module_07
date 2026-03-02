from abc import ABC, abstractmethod


class Rankable(ABC):
    def __init__(self, rating: int, wins: int, losses: int, **kwargs) -> None:
        super().__init__(**kwargs)
        self._rating = rating
        self._wins = wins
        self._losses = losses

    @abstractmethod
    def calculate_rating(self) -> int:
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        pass

    @abstractmethod
    def get_rank_info(self) -> dict:
        pass
