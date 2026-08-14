import random


ACHIEVEMENTS: list[str] = [
    "First Steps",
    "Boss Slayer",
    "Master Explorer",
    "Treasure Hunter",
    "Survivor",
    "Strategist",
    "Speed Runner",
    "World Savior",
    "Crafting Genius",
    "Collector Supreme",
    "Untouchable",
    "Unstoppable",
    "Sharp Mind",
    "Hidden Path Finder",
]


def gen_player_achievements() -> set[str]:
    amount = random.randint(5, 10)
    selected: list[str] = random.sample(ACHIEVEMENTS, amount)
    player_achievements: set[str] = set(selected)
    return player_achievements


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")

    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    all_available: set[str] = set(ACHIEVEMENTS)

    all_distinct = alice.union(
        bob,
        charlie,
        dylan,
    )

    common_achievements = alice.intersection(
        bob,
        charlie,
        dylan,
    )

    only_alice = alice.difference(
        bob,
        charlie,
        dylan,
    )
    only_bob = bob.difference(
        alice,
        charlie,
        dylan,
    )
    only_charlie = charlie.difference(
        alice,
        bob,
        dylan,
    )
    only_dylan = dylan.difference(
        alice,
        bob,
        charlie,
    )

    alice_missing = all_available.difference(alice)
    bob_missing = all_available.difference(bob)
    charlie_missing = all_available.difference(charlie)
    dylan_missing = all_available.difference(dylan)

    print("\nPlayer Alice:", alice)
    print("Player Bob:", bob)
    print("Player Charlie:", charlie)
    print("Player Dylan:", dylan)

    print("\nAll distinct achievements:", all_distinct)
    print("\nCommon achievements:", common_achievements)

    print("\nOnly Alice has:", only_alice)
    print("Only Bob has:", only_bob)
    print("Only Charlie has:", only_charlie)
    print("Only Dylan has:", only_dylan)

    print("\nAlice is missing:", alice_missing)
    print("Bob is missing:", bob_missing)
    print("Charlie is missing:", charlie_missing)
    print("Dylan is missing:", dylan_missing)
