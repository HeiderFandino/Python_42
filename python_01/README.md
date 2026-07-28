# Python 01 - Code Cultivation

Introduction to object-oriented programming in Python through the development
of a digital garden ecosystem.

This project is part of the Python modules at 42 Barcelona. Across seven
progressive exercises, a basic plant representation evolves into a reusable
class hierarchy with validation, inheritance, polymorphism and analytics.

## Learning objectives

- Structure and execute Python programs.
- Create classes, objects, attributes and methods.
- Initialize objects with `__init__()`.
- Modify and protect object state.
- Apply encapsulation with getters, setters and validation.
- Reuse behavior through inheritance and `super()`.
- Override methods and use polymorphism.
- Work with `@staticmethod` and `@classmethod`.
- Build nested classes and multilevel inheritance.
- Add type hints and validate them with `mypy`.
- Follow Python style conventions with `flake8`.

## Project structure

```text
python_01/
├── ex0/
│   └── ft_garden_intro.py
├── ex1/
│   └── ft_garden_data.py
├── ex2/
│   └── ft_plant_growth.py
├── ex3/
│   └── ft_plant_factory.py
├── ex4/
│   └── ft_garden_security.py
├── ex5/
│   └── ft_plant_types.py
└── ex6/
    └── ft_garden_analytics.py
```

## Exercises

| Exercise | Description | Main concepts |
| --- | --- | --- |
| `ex0` | Displays basic information about a plant. | Variables, program entry point, `__name__` |
| `ex1` | Organizes several plants using a common model. | Classes, objects, attributes, methods |
| `ex2` | Simulates plant growth over one week. | Object state, `grow()`, `age()`, loops |
| `ex3` | Creates fully initialized plants. | Constructors, `__init__()` |
| `ex4` | Protects plant data from invalid values. | Encapsulation, validation, getters, setters |
| `ex5` | Adds flowers, trees and vegetables. | Inheritance, `super()`, overriding, polymorphism |
| `ex6` | Adds plant statistics and a `Seed` type. | Nested classes, `staticmethod`, `classmethod`, multilevel inheritance |

## Requirements

- Python 3.10 or later
- `flake8`
- `mypy`

Install the development tools with:

```bash
python3 -m pip install flake8 mypy
```

## Usage

Run an exercise from the repository root:

```bash
python3 ex0/ft_garden_intro.py
python3 ex1/ft_garden_data.py
python3 ex2/ft_plant_growth.py
python3 ex3/ft_plant_factory.py
python3 ex4/ft_garden_security.py
python3 ex5/ft_plant_types.py
python3 ex6/ft_garden_analytics.py
```

## Code quality

Check style and type annotations across all exercises:

```bash
flake8 ex0 ex1 ex2 ex3 ex4 ex5 ex6
mypy ex0 ex1 ex2 ex3 ex4 ex5 ex6
```

## Key class hierarchy

```text
Plant
├── Flower
│   └── Seed
├── Tree
└── Vegetable
```

`Plant` contains the shared state and behavior. Specialized classes extend it
with their own attributes and actions while reusing the common implementation.

## Author

**Heider Fandiño**  
42 Barcelona student - `hfandino`
