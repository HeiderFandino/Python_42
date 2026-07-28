def input_temperature(temp_str: str) -> int:
    temperature = (int(temp_str))

    if temperature > 40:
        raise ValueError(
                f"{temperature}ºC is too hot for plants (max 40ºC)"
        )
    if temperature < 0:
        raise ValueError(
                f"{temperature}ºC is too cold for plants (min 0ºC)"
        )
    return temperature


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    print()

    valid_data = "25"
    print(f"Input data is '{valid_data}'")
    temperature = input_temperature(valid_data)
    print("Temperature now is", temperature, "ºC")
    print()

    invalid_data = "abc"
    print(f"Input data is '{invalid_data}'")
    try:
        input_temperature(invalid_data)
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")
    print()

    hot_data = "100"
    print(f"Input data is '{hot_data}'")
    try:
        input_temperature(hot_data)
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")
    print()

    cold_data = "-50"
    print(f"Input data is '{cold_data}'")
    try:
        input_temperature(cold_data)
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")
    print()

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
