import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        user_input = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )
        parameters = user_input.split(",")

        if len(parameters) != 3:
            print("Invalid syntax")
            continue

        coordinates: list[float] = []

        for parameter in parameters:
            try:
                coordinate = float(parameter)
                coordinates += [coordinate]
            except ValueError as error:
                print(f"Error on parameter '{parameter}': {error}")
                break

        if len(coordinates) != 3:
            continue

        position: tuple[float, float, float] = (
            coordinates[0],
            coordinates[1],
            coordinates[2],
        )
        return position


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print()

    print("Get a first set of coordinates")
    player_position = get_player_pos()

    print(f"Got a first tuple: {player_position}")
    print(
        f"It includes: X={player_position[0]}, "
        f"Y={player_position[1]}, "
        f"Z={player_position[2]}"
    )

    distance_to_center = math.sqrt(
        player_position[0] ** 2
        + player_position[1] ** 2
        + player_position[2] ** 2
    )

    print(f"Distance to center: {round(distance_to_center, 4)}")
    print()

    print("Get a second set of coordinates")
    new_position = get_player_pos()

    distance_between = math.sqrt(
        (new_position[0] - player_position[0]) ** 2
        + (new_position[1] - player_position[1]) ** 2
        + (new_position[2] - player_position[2]) ** 2
    )

    print(
        "Distance between the 2 sets of coordinates: "
        f"{round(distance_between, 4)}"
    )
