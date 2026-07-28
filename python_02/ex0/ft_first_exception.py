def input_temperature(tem_str: str) -> int:
    return (int(tem_str))


def test_temperature():
    print("=== Garden Temperature ===")
    print()

    valid_data = "25"
    print(f"Input data is '{valid_data}'")
    temperature = input_temperature(valid_data)
    print(f"Temperature is now {temperature}ºC")
    print()

    invalid_data = "abc"
    print(f"Input data is '{invalid_data}'")

    try:
        input_temperature(invalid_data)
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")

    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
