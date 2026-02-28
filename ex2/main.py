from .EliteCard import EliteCard


if __name__ == "__main__":
    print("\n === DataDeck Ability System ===\n")

    print("EliteCard capabilities:")

    arcane_warrior = EliteCard("Arcane Warrior", 5, "melee", 5, 10, 3, 8)
    enemy = EliteCard("Enemy", 1, "melee", 5, 10, 2, 10)
    enemy1 = EliteCard("Enemy1", 1, "melee", 5, 10, 2, 10)
    enemy2 = EliteCard("Enemy2", 1, "melee", 5, 10, 2, 10)
    card_methods = ["play", "get_card_info", "is_playable"]
    combatable_methods = ["attack", "defend", "get_combat_stats"]
    magical_methods = ["cast_spell", "channel_mana", "get_magic_stats"]
    targets = [enemy1, enemy2]

    print(f"- Card: {card_methods}")
    print(f"- Combatable: {combatable_methods}")
    print(f"- Magical: {magical_methods}")

    print("\nPlaying Arcane Warrior (Elite Card):\n")

    print("Combat phase:")
    print(f"Attack result: {arcane_warrior.attack(enemy)}")
    print(f"Defense result: {arcane_warrior.defend(5)}")

    print("\nMagic Phase:")
    print(f"Spell cast: {arcane_warrior.cast_spell("Fireball", targets)}")
    print(f"Mana channel: {arcane_warrior.channel_mana(5)}")

    print("\nMultiple interface implementation successful!")
