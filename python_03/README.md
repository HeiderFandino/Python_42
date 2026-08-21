# Python Module 03 - Data Quest

Python Module 03 is a collection-focused project completed as part of the 42 Barcelona curriculum. Set in a game analytics environment, the module introduces Python's core collection types and progressively applies them to command-line data, coordinates, achievements, inventories, event streams, and data transformations.

The project moves from basic list access to tuples, sets, dictionaries, generators, and comprehensions, with an emphasis on choosing the right data structure for each problem.

## Learning objectives

- Access and process command-line arguments through `sys.argv`.
- Store and analyze numeric data with lists.
- Represent immutable 3D coordinates with tuples.
- Perform union, intersection, and difference operations with sets.
- Model key-value data with dictionaries.
- Generate values on demand with `yield`.
- Transform and filter collections with comprehensions.
- Handle invalid input gracefully.
- Validate Python code with `flake8` and `mypy`.

## General requirements

- Python 3.10 or later.
- Code must comply with `flake8`.
- Functions and methods must include type hints and pass `mypy`.
- Exceptions must be handled gracefully.
- No file I/O operations are allowed.
- Data must be processed in memory or through command-line arguments.
- Each exercise must clearly demonstrate the required collection operations.

## Project structure

```text
python_03/
├── ex0/
│   └── ft_command_quest.py
├── ex1/
│   └── ft_score_analytics.py
├── ex2/
│   └── ft_coordinate_system.py
├── ex3/
│   └── ft_achievement_tracker.py
├── ex4/
│   └── ft_inventory_system.py
├── ex5/
│   └── ft_data_stream.py
├── ex6/
│   └── ft_data_alchemist.py
└── README.md
```

## Exercises

### ex0 - Command Quest

Displays the program name and all values received through the command line. This exercise introduces list access through `sys.argv`.

Main concepts:

- `sys.argv`
- List indexing
- List iteration
- Argument counting
- Quoted command-line values

Usage:

```bash
python3 ex0/ft_command_quest.py hello world 42
python3 ex0/ft_command_quest.py "Data Quest"
```

### ex1 - Score Cruncher

Parses game scores from command-line arguments, discards invalid values, stores valid scores in a list, and calculates player statistics.

Calculated metrics:

- Number of players
- Total score
- Average score
- Highest score
- Lowest score
- Score range

Main concepts:

- List creation and iteration
- Numeric conversion
- `try` and `except`
- Partial recovery from invalid input
- `sum()`, `max()`, and `min()`

Usage:

```bash
python3 ex1/ft_score_analytics.py 1500 2300 1800 2100 1950
```

### ex2 - Position Tracker

Reads two sets of 3D coordinates, stores them as tuples, and calculates distances to the origin and between both positions.

Main concepts:

- Tuple creation and unpacking
- Immutable coordinate data
- Input validation and retry loops
- Floating-point conversion
- Euclidean distance
- `math.sqrt()` and `round()`

Usage:

```bash
python3 ex2/ft_coordinate_system.py
```

The expected coordinate format is:

```text
x,y,z
```

### ex3 - Achievement Hunter

Generates achievement sets for at least four players and analyzes relationships across their collections.

The program identifies:

- All distinct achievements.
- Achievements shared by every player.
- Achievements unique to each player.
- Achievements missing from each player.

Main concepts:

- Set uniqueness
- Random selection
- `set.union()`
- `set.intersection()`
- `set.difference()`
- Empty set representation

Usage:

```bash
python3 ex3/ft_achievement_tracker.py
```

Output varies because achievements are assigned randomly.

### ex4 - Inventory Master

Parses command-line values in `<item_name>:<quantity>` format and stores valid inventory entries in a dictionary. Invalid syntax, invalid quantities, and duplicate items are discarded with appropriate messages.

The program reports:

- The complete inventory.
- A list of item names.
- Total item quantity.
- Percentage represented by each item.
- Most and least abundant items.
- An updated inventory containing a new item.

Main concepts:

- Dictionary creation and update
- Key-value parsing
- Duplicate detection
- `dict.keys()` and `dict.values()`
- Aggregation and percentages
- Tie handling based on input order

Usage:

```bash
python3 ex4/ft_inventory_system.py \
  sword:1 potion:5 shield:2 armor:3 helmet:1
```

### ex5 - Stream Wizard

Implements generators that produce game events on demand instead of storing an endless stream in memory.

The exercise includes:

- An endless event generator returning `(player, action)` tuples.
- Consumption of 1,000 generated events.
- Creation of a list containing 10 events.
- A second generator that randomly removes and yields events until the list is empty.

Main concepts:

- Generator functions
- `yield`
- `next()`
- Lazy evaluation
- Infinite streams
- Iteration with `for ... in ...`
- `typing.Generator`

Usage:

```bash
python3 ex5/ft_data_stream.py
```

### ex6 - Data Alchemist

Uses list and dictionary comprehensions to transform and filter player data.

The program creates:

- A normalized list in which every player name is capitalized.
- A filtered list containing names that were already capitalized.
- A score dictionary built from the normalized names.
- A filtered dictionary containing scores above the average.

Main concepts:

- List comprehensions
- Dictionary comprehensions
- Transformation and filtering
- Random score generation
- Average calculation

Usage:

```bash
python3 ex6/ft_data_alchemist.py
```

Each comprehension should remain on a single line unless it exceeds the permitted line length.

## Collection overview

| Collection | Ordered | Mutable | Unique values | Typical use in this module |
|---|---|---|---|---|
| `list` | Yes | Yes | No | Scores and command-line data |
| `tuple` | Yes | No | No | Fixed 3D coordinates and events |
| `set` | No | Yes | Yes | Achievement relationships |
| `dict` | Yes | Yes | Keys only | Inventory and score mappings |
| Generator | Sequential | Stateful | Not applicable | On-demand event streams |

## Verification

Run the linter and static type checker from the project root:

```bash
flake8 ex0/ft_command_quest.py \
  ex1/ft_score_analytics.py \
  ex2/ft_coordinate_system.py \
  ex3/ft_achievement_tracker.py \
  ex4/ft_inventory_system.py \
  ex5/ft_data_stream.py \
  ex6/ft_data_alchemist.py

mypy ex0/ft_command_quest.py \
  ex1/ft_score_analytics.py \
  ex2/ft_coordinate_system.py \
  ex3/ft_achievement_tracker.py \
  ex4/ft_inventory_system.py \
  ex5/ft_data_stream.py \
  ex6/ft_data_alchemist.py
```

Recommended manual cases:

- No command-line arguments.
- Mixed valid and invalid scores.
- Invalid coordinate syntax and invalid numeric values.
- Random achievement sets with empty and non-empty relationships.
- Duplicate and malformed inventory entries.
- Complete generator consumption.
- Comprehension outputs and average-score filtering.

## Key takeaway

Python collections are not interchangeable containers. Their behavior determines how efficiently and clearly a program can model a problem. This module demonstrates how lists, tuples, sets, dictionaries, generators, and comprehensions solve different data-processing tasks.

Developed as part of the 42 Barcelona curriculum.
