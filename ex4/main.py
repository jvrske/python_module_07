from .TournamentCard import TournamentCard
from .TournamentPlatform import TournamentPlatform

if __name__ == "__main__":
    print("\n=== DataDeck Tournament Platform ===\n")

    print("Registering Tournament Cards...\n")

    card_1 = TournamentCard("dragon_001", "Fire Dragon", 1200)
    card_2 = TournamentCard("wizard_001", "Ice Wizard", 1150)
    platform = TournamentPlatform()

    print(platform.register_card(card_1))
    print()
    print(platform.register_card(card_2))

    print("\nCreating tournament match...")
    result = platform.create_match("dragon_001", "wizard_001")
    print(f"Match result: {result}")

    print("\nTournament Leaderboard:")
    for line in platform.get_leaderboard():
        print(line)

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")
