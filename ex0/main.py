from CreatureCard import CreatureCard


if __name__ == "__main__":
    print("\n=== DataDeck Card Foundation ===\n")

    print("Testing Abstract Base Class Design\n")
    card1 = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    print("CreatureCard Info:")
    print(card1.get_card_info())

    mana_available = 6
    print(f"\nPlaying {card1.get_card_info()['name']} with {mana_available} \
mana available:")
    print(f"Playable: {card1.is_playable(mana_available)}")
    print(f"Play Result {card1.play({"mana": mana_available})}")

    print(f"\n{card1.get_card_info()['name']} attacks Goblin Warrior:")
    print(f"Attack result: {card1.attack_target("Goblin Warrior")}")

    mana_available = 3
    print(f"\nTesting insufficient mana ({mana_available} available)")
    print(f"Playable: {card1.is_playable(mana_available)}")

    print("\nAbstract pattern successfully demonstrated!")
