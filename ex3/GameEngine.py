from .CardFactory import CardFactory
from .GameStrategy import GameStrategy


class GameEngine():
    def __init__(self) -> None:
        self.factory = None
        self.strategy = None
        self.hand = []
        self.battlefield = []
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy
        self.hand = [
            self.factory.create_creature("dragon"),
            self.factory.create_creature("goblin"),
            self.factory.create_spell("lightning_bolt")
        ]
        self.cards_created = len(self.hand)

    def simulate_turn(self) -> dict:
        self.strategy.prioritize_targets(["Enemy Player"])
        result = self.strategy.execute_turn(self.hand, self.battlefield)
        dmg = int(result.get("actions", {}).get("damage_dealt", 0))
        self.total_damage += dmg
        self.turns_simulated += 1
        return result

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_damage,
            "cards_created": self.cards_created
        }
