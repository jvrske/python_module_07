from .Deck import Deck
from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard
from ex0.CreatureCard import CreatureCard


if __name__ == "__main__":
    print("\n=== DataDeck Deck Builder ===\n")

    print("Building deck with different card types...")
    creature_card = CreatureCard("Fire Dragon", 5, "Legendary", 5, 7)
    spell_card = SpellCard("Lightning Bold", 3, "Common",
                           "Deal 3 damage to target")
    artifact_card = ArtifactCard("Mana Crystal", 4, "Common", 1,
                                 "Permanent: +1 mana per turn")
    deck = Deck()

    for type in creature_card, spell_card, artifact_card:
        deck.add_card(type)
    print(f"Deck stats: {deck.get_deck_stats()}")

    print("\nDrawing and playing cards:\n")

    mana = 20
    deck.shuffle()
    for i in range(len(deck._deck)):
        draw_card = deck.draw_card()
        if isinstance(draw_card, CreatureCard):
            print(f"Drew: {draw_card._name} (Creature)")
        elif isinstance(draw_card, SpellCard):
            print(f"Drew: {draw_card._name} (Spell)")
        elif isinstance(draw_card, ArtifactCard):
            print(f"Drew: {draw_card._name} (Artifact)")

        is_playable = draw_card.is_playable(mana)
        if is_playable:
            print(f"Play result: {draw_card.play({'mana': mana})}\n")

    print("Polymorphism in action: Same interface, different card behaviors!")
