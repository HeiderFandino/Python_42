# Python Module 02 - Garden Guardian

Python Module 02 is an exception-handling project completed as part of the 42 Barcelona curriculum. Set in a smart agriculture environment, the module focuses on building resilient programs that validate sensor data, distinguish failure modes, define domain-specific exceptions, and guarantee cleanup.

Each exercise adds another layer of defensive programming, progressing from catching a conversion error to building an exception hierarchy and using `finally` for reliable resource cleanup.

## Learning objectives

- Handle runtime failures with `try` and `except`.
- Convert invalid input into controlled program behavior.
- Raise exceptions deliberately with `raise`.
- Catch specific and multiple exception types.
- Create custom exception classes.
- Organize related exceptions through inheritance.
- Guarantee cleanup with `finally`.
- Keep programs running safely after expected failures.
- Validate code with `flake8` and `mypy`.

## General requirements

- Python 3.10 or later.
- Code must comply with `flake8`.
- All functions and methods must include type hints.
- Every exercise must demonstrate `try`/`except` error handling.
- Built-in exception types may be used when appropriate.
- Programs must demonstrate both normal and error scenarios.
- Programs must never crash during the expected test cases.
- Solutions should remain simple and focused on the required concepts.

## Project structure

```text
python_02/
├── ex0/
│   └── ft_first_exception.py
├── ex1/
│   └── ft_raise_exception.py
├── ex2/
│   └── ft_different_errors.py
├── ex3/
│   └── ft_custom_errors.py
├── ex4/
│   └── ft_finally_block.py
└── README.md
```

## Exercises

### ex0 - Agricultural Data Validation

Introduces basic exception handling through temperature conversion.

The exercise defines:

- `input_temperature()`, which converts a sensor reading from `str` to `int`.
- `test_temperature()`, which tests valid and invalid values without stopping the program.

Main concepts:

- Numeric conversion with `int()`
- Conversion failures
- `try` and `except`
- Exception messages
- Program continuation after failure

Usage:

```bash
python3 ex0/ft_first_exception.py
```

### ex1 - Agricultural Data Validation Pipeline

Extends `ex0` by validating whether a converted temperature is suitable for plants. Valid temperatures are between `0` and `40` degrees Celsius, inclusive.

The function must:

- Return values inside the accepted range.
- Raise an exception when the temperature is too low.
- Raise an exception when the temperature is too high.
- Continue handling non-numeric input from the previous exercise.

Main concepts:

- Explicit `raise`
- Range validation
- Reusing exception-handling logic
- Separating validation from error presentation

Usage:

```bash
python3 ex1/ft_raise_exception.py
```

### ex2 - Different Types of Problems

Demonstrates that different failures should be represented and handled by different exception types.

`garden_operations()` intentionally produces:

- `ValueError`
- `ZeroDivisionError`
- `FileNotFoundError`
- `TypeError`

Other operation values complete normally. `test_error_types()` executes every case, catches each failure, and demonstrates catching multiple exception types with one `try` block.

Main concepts:

- Specific exception handling
- Multiple `except` branches
- Catching multiple types together
- Deliberately faulty code for testing
- Successful fall-through behavior

Usage:

```bash
python3 ex2/ft_different_errors.py
```

The intentional `TypeError` case is expected to be reported by `mypy`. In this exercise, that static analysis warning confirms that `mypy` detected the deliberately invalid operation.

### ex3 - Making Your Own Error Types

Introduces custom exception classes for garden-specific failures.

Required hierarchy:

```text
Exception
└── GardenError
    ├── PlantError
    └── WaterError
```

Each custom exception provides a default message when no message is supplied. The program demonstrates both specific catches and a general `GardenError` catch that handles all related failures.

Main concepts:

- Custom exception classes
- Exception inheritance
- Default error messages
- Domain-specific error semantics
- Catching parent and child exception types

Usage:

```bash
python3 ex3/ft_custom_errors.py
```

### ex4 - Finally Block: Always Clean Up

Uses the custom `PlantError` concept from `ex3` to model a watering system that must always close, even when an invalid plant name interrupts the test.

The program demonstrates:

- Successful watering for capitalized plant names.
- A raised `PlantError` for invalid names.
- Early return after an error.
- Guaranteed cleanup through `finally`.

Main concepts:

- `try`/`except`/`finally`
- Cleanup guarantees
- Early `return` inside protected logic
- Custom exceptions in application code
- Capitalization validation

Usage:

```bash
python3 ex4/ft_finally_block.py
```

## Exception flow

```text
try
├── operation succeeds
│   └── continue normally
└── operation raises an exception
    └── matching except handles it

finally
└── always executes before leaving the structure
```

`finally` executes after success, after a handled exception, and even before an early `return` leaves the function.

## Built-in and custom exceptions

| Exception | Typical meaning in this module |
|---|---|
| `ValueError` | A value has the correct general type but invalid content |
| `ZeroDivisionError` | A calculation attempts division by zero |
| `FileNotFoundError` | A requested path does not exist |
| `TypeError` | An operation combines incompatible types |
| `GardenError` | Base class for garden-specific failures |
| `PlantError` | Invalid plant-related state or input |
| `WaterError` | Watering-system failure |

## Verification

Run each script and confirm that every expected failure is caught without terminating the program:

```bash
python3 ex0/ft_first_exception.py
python3 ex1/ft_raise_exception.py
python3 ex2/ft_different_errors.py
python3 ex3/ft_custom_errors.py
python3 ex4/ft_finally_block.py
```

Run `flake8` from the project root:

```bash
flake8 ex0/ft_first_exception.py \
  ex1/ft_raise_exception.py \
  ex2/ft_different_errors.py \
  ex3/ft_custom_errors.py \
  ex4/ft_finally_block.py
```

Run `mypy` individually so the intentional `TypeError` in `ex2` can be distinguished from unexpected type-checking failures:

```bash
mypy ex0/ft_first_exception.py
mypy ex1/ft_raise_exception.py
mypy ex2/ft_different_errors.py
mypy ex3/ft_custom_errors.py
mypy ex4/ft_finally_block.py
```

Recommended manual cases:

- Valid numeric temperature.
- Non-numeric temperature.
- Temperatures below and above the accepted range.
- Every intentional built-in exception in `ex2`.
- Default and custom messages for each custom exception.
- Catching `PlantError` and `WaterError` through `GardenError`.
- Successful watering sequence.
- Invalid plant name followed by guaranteed cleanup.

## Key takeaway

Reliable programs do not assume that every operation will succeed. They classify failures, preserve useful error information, recover when possible, and always clean up critical resources. This module builds those habits through Python's exception-handling system.

Developed as part of the 42 Barcelona curriculum.
