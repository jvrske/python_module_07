from .FantasyCardFactory import FantasyCardFactory
from .AggressiveStrategy import AggressiveStrategy
from .GameEngine import GameEngine


if __name__ == "__main__":
    print("\n === DataDeck Game Engine ===\n")

    print("Configuring Fantasy Card Game...")
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()

    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Available types: {factory.get_supported_types()}")

    print("\nSimulating aggressive turn...")
    engine.configure_engine(factory, strategy)
    print(
        "Hand: ["
        + ", ".join(f"{c._name} ({c._cost})" for c in engine.hand)
        + "]"
    )

    turn = engine.simulate_turn()
    print("Turn execution:")
    print(f"Strategy: {turn.get('strategy')}")
    print(f"Actions: {turn.get('actions')}")

    print("\nGame Report:")
    print(engine.get_engine_status())

    print("\nAbstract Factory + Strategy Pattern: Maximum flexibility \
achieved!")
