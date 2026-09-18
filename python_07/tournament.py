from ex0 import AquaFactory, CreatureFactory, FlameFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    AggressiveStrategy,
    BattleStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
    NormalStrategy,
)


def battle(
    opponents: list[tuple[CreatureFactory, BattleStrategy]],
) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            first_factory, first_strategy = opponents[i]
            second_factory, second_strategy = opponents[j]

            first_creature = first_factory.create_base()
            second_creature = second_factory.create_base()

            print()
            print("* Battle *")
            print(first_creature.describe())
            print(" vs.")
            print(second_creature.describe())
            print(" now fight!")

            try:
                first_strategy.act(first_creature)
                second_strategy.act(second_creature)
            except InvalidStrategyError as error:
                print(f"Battle error, aborting tournament: {error}")
                return


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    battle([
        (flame_factory, normal),
        (healing_factory, defensive),
    ])

    print()
    print("Tournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([
        (flame_factory, aggressive),
        (healing_factory, defensive),
    ])

    print()
    print("Tournament 2 (multiple)")
    print(
        " [ (Aquabub+Normal), (Healing+Defensive), "
        "(Transform+Aggressive) ]"
    )
    battle([
        (aqua_factory, normal),
        (healing_factory, defensive),
        (transform_factory, aggressive),
    ])


if __name__ == "__main__":
    main()
