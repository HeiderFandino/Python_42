import ex0


def test_factory(factory: ex0.CreatureFactory) -> None:
    print("Testing factory")

    creature = factory.create_base()
    creature_evolved = factory.create_evolved()

    print(creature.describe())
    print(creature.attack())
    print(creature_evolved.describe())
    print(creature_evolved.attack())
    print()


def battle(
    first_factory: ex0.CreatureFactory,
    second_factory: ex0.CreatureFactory,
) -> None:
    print("Testing battle")

    first_creature = first_factory.create_base()
    second_creature = second_factory.create_base()

    print(first_creature.describe())
    print(" vs.")
    print(second_creature.describe())
    print(" fight!")
    print(first_creature.attack())
    print(second_creature.attack())


def main() -> None:
    flame_factory = ex0.FlameFactory()
    aqua_factory = ex0.AquaFactory()

    test_factory(flame_factory)
    test_factory(aqua_factory)

    battle(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()
