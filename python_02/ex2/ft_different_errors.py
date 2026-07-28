def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    if operation_number == 1:
        1 / 0
    if operation_number == 2:
        open("/non/existent/file", "r")
    if operation_number == 3:
        "a" + 1


def test_error_types() -> None:
    number_operation = 0
    print("=== Garden Error Types Demo ===")
    while number_operation < 5:
        print(f"Testing operation {number_operation}...")
        try:
            garden_operations(number_operation)
        except ValueError as error:
            print(f"Caught ValueError: {error}")
        except ZeroDivisionError as error:
            print(f"Caught ZeroDivisionError: {error}")
        except FileNotFoundError as error:
            print(f"Caught FileNotFoundError: {error}")
        except TypeError as error:
            print(f"Caught TypeError: {error}")
        else:
            print("Operation completed successfully")
        number_operation += 1
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
