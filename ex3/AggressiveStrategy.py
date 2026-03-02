from .GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def __init__(self) -> None:
        self._targets = []

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        cards_played = []
        mana_used = 0
        damage_dealt = 0

        if len(hand) > 0:
            card = hand.pop(0)
            battlefield.append(card)

            name = getattr(card, "_name", getattr(card, "name", str(card)))
            cost = getattr(card, "_cost", getattr(card, "cost", 0))

            cards_played.append(name)
            mana_used += int(cost)

            attack = getattr(card, "_attack", None)
            if attack is not None:
                damage_dealt += int(attack) + 1
            else:
                damage_dealt += int(cost) + 1

        return {
            "strategy": self.get_strategy_name(),
            "actions": {
                "cards_played": cards_played,
                "mana_used": mana_used,
                "targets_attacked": self._targets,
                "damage_dealt": damage_dealt,
            },
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        if available_targets is None or len(available_targets) == 0:
            self._targets = ["Enemy Player"]
        else:
            self._targets = list(available_targets)
        return self._targets
