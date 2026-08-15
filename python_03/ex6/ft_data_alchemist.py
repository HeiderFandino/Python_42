import random


if __name__ == "__main__":
    list_of_players: list[str] = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam",
    ]

    capitalized_players: list[str] = [
        player.capitalize() for player in list_of_players
    ]

    only_capitalized: list[str] = [
        player for player in list_of_players if player.istitle()
    ]

    score_dict: dict[str, int] = {
        player: random.randint(0, 1000)
        for player in capitalized_players
    }

    score_average: float = (
        sum(score_dict.values()) / len(score_dict)
    )

    high_scores: dict[str, int] = {
        player: score
        for player, score in score_dict.items()
        if score > score_average
    }

    print("=== Game Data Alchemist ===")

    print("\nInitial list of players:", list_of_players)
    print(
        "New list with all names capitalized:",
        capitalized_players,
    )
    print(
        "New list of capitalized names only:",
        only_capitalized,
    )

    print("\nScore dict:", score_dict)
    print("Score average is", round(score_average, 2))
    print("High scores:", high_scores)
