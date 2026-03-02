from .TournamentCard import TournamentCard


class TournamentPlatform():
    def __init__(self):
        self._cards: dict[str, TournamentCard] = {}
        self.match_played = 0

    def register_card(self, card: TournamentCard) -> str:
        self._cards[card.card_id] = card

        return (
            f"{card._name} (ID: {card.card_id}):\n"
            f"- Interfaces: [Card, Combatable, Rankable]\n"
            f"- Rating: {card.calculate_rating()}\n"
            f"- Record: {card._wins}-{card._losses}"
        )

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self._cards[card1_id]
        card2 = self._cards[card2_id]
        self.match_played += 1

        winner = card1
        loser = card2

        winner.update_wins(1)
        loser.update_losses(1)

        winner_rating = winner.calculate_rating()
        loser_rating = loser.calculate_rating()

        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner_rating,
            "loser_rating": loser_rating,
        }

    def _sort_by_rating(self, card):
        return card._rating

    def get_leaderboard(self) -> list:
        cards = list(self._cards.values())
        cards.sort(key=self._sort_by_rating, reverse=True)

        leaderboard_lines = []
        position = 1

        for c in cards:
            line = f"{position}. {c._name} - Rating: {c._rating} \
({c._wins}-{c._losses})"
            leaderboard_lines.append(line)
            position += 1

        return leaderboard_lines

    def generate_tournament_report(self) -> dict:
        avg_rating = 0
        for card in self._cards.values():
            avg_rating += card._rating
        average = (round(avg_rating / len(self._cards)))
        return {
            "total_cards": len(self._cards),
            "matches_played": self.match_played,
            "avg_rating": average,
            "platform_status": "active"
        }
