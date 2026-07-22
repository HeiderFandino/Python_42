# Python 00 — Growing Code

Introduction to Python fundamentals through a series of small exercises based on community garden scenarios.

This module focuses on learning Python's basic syntax and semantics: functions, variables, user input, arithmetic operations, conditional statements, loops, recursion, string methods, and type annotations.

## Learning objectives

- Understand the basic syntax of Python.
- Define and call functions.
- Read user input with `input()`.
- Convert strings to integers with `int()`.
- Work with variables and arithmetic operations.
- Control program flow with `if`, `elif`, and `else`.
- Repeat operations using iterative and recursive approaches.
- Use string methods.
- Add type annotations and check them with `mypy`.
- Write clean code that follows `flake8` standards.

## Exercises

| Exercise | Function | Main concept |
|---|---|---|
| `ex0` | `ft_hello_garden` | Functions and output with `print()` |
| `ex1` | `ft_garden_name` | User input and variables |
| `ex2` | `ft_plot_area` | Integer conversion and arithmetic |
| `ex3` | `ft_harvest_total` | Accumulating and displaying values |
| `ex4` | `ft_plant_age` | Conditional statements |
| `ex5` | `ft_water_reminder` | Comparisons and decision making |
| `ex6` | `ft_count_harvest_iterative` | Iteration and counting |
| `ex6` | `ft_count_harvest_recursive` | Recursion and base cases |
| `ex7` | `ft_seed_inventory` | Parameters, string methods, and type hints |

## Repository structure

```text
Python-00/
├── README.md
├── ex0/
│   └── ft_hello_garden.py
├── ex1/
│   └── ft_garden_name.py
├── ex2/
│   └── ft_plot_area.py
├── ex3/
│   └── ft_harvest_total.py
├── ex4/
│   └── ft_plant_age.py
├── ex5/
│   └── ft_water_reminder.py
├── ex6/
│   ├── ft_count_harvest_iterative.py
│   └── ft_count_harvest_recursive.py
└── ex7/
    └── ft_seed_inventory.py
```

## Project rules

- The project must use Python 3.10 or later.
- Each exercise must be stored in its specified directory and file.
- Files must contain only the requested functions; no standalone main program is required.
- Function and file names must match the subject exactly.
- Code must comply with `flake8`.
- Type hints are recommended from `ex0` to `ex6` and required in `ex7`.
- Input validation is not required unless explicitly requested by the subject.

## Running the exercises

The subject provides a helper `main.py` that imports and tests the functions. Place it in the appropriate working directory and run:

```bash
python3 main.py
```

Individual files contain functions rather than standalone programs, so they are intended to be imported and called by the provided tester.

## Code quality checks

Check formatting and common style issues:

```bash
flake8 ex0 ex1 ex2 ex3 ex4 ex5 ex6 ex7
```

Check the required type annotations in the final exercise:

```bash
mypy ex7/ft_seed_inventory.py
```

## Key takeaways

Python removes much of the explicit syntax and manual memory management required in C, but the underlying problem-solving process remains the same: understand the input, define the logic, handle each condition, and produce the exact expected output.

The most important lessons from this module are the distinction between syntax and logic, the role of indentation in Python, and the difference between solving a repeated task iteratively and recursively.

---

Part of my [`python-42`](../README.md) repository, which contains the Python modules completed during my studies at 42 Barcelona.
