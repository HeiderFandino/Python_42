# Python Module 04 - Data Archivist

Python Module 04 is a file-handling project completed as part of the 42 Barcelona curriculum. The module follows a cyber-archive theme and introduces progressively safer ways to read, transform, write, and manage text files in Python.

The exercises build on one another, moving from manual file handling to standard streams and, finally, context managers.

## Learning objectives

- Open, read, write, and close text files.
- Handle filesystem errors without crashing unexpectedly.
- Transform file content line by line.
- Work with `stdin`, `stdout`, and `stderr`.
- Redirect program output and errors independently.
- Use `with` to manage file resources safely.
- Design a typed function with a stable `tuple[bool, str]` return contract.
- Validate code with `flake8` and `mypy`.

## General requirements

- Python 3.10 or later.
- Code must comply with `flake8`.
- Functions and methods must include type hints and pass `mypy`.
- Exceptions must be handled gracefully.
- `with` must not be used before `ex3`.

## Project structure

```text
python_04/
├── ex0/
│   └── ft_ancient_text.py
├── ex1/
│   └── ft_archive_creation.py
├── ex2/
│   └── ft_stream_management.py
├── ex3/
│   └── ft_vault_security.py
└── README.md
```

## Exercises

### ex0 - Ancient Text Recovery

Reads a filename from the command line, opens the file, displays its content, and handles errors such as missing or inaccessible files.

Main concepts:

- `sys.argv`
- `open()` and `read()`
- Manual `close()`
- `try`, `except`, and `else`
- `OSError`
- `typing.IO[str]`

Usage:

```bash
python3 ex0/ft_ancient_text.py ancient_fragment.txt
```

### ex1 - Archive Creation

Extends `ex0` by transforming the recovered content. A `#` archive marker is added to each line, and the user may save the transformed data to a new file.

Main concepts:

- Line-by-line text transformation
- `splitlines()`
- String accumulation
- `input()`
- Write mode (`"w"`)
- `write()` and manual `close()`

Usage:

```bash
python3 ex1/ft_archive_creation.py ancient_fragment.txt
```

Leaving the destination filename empty skips the save operation. Providing a filename creates the file or replaces its existing content.

### ex2 - Stream Management

Reworks the previous exercise using the three standard streams. Exception messages are sent to `stderr`, while user input is read directly from `stdin` without using `input()`.

Main concepts:

- `sys.stdin`
- `sys.stdout`
- `sys.stderr`
- `readline()`
- `write()` and `flush()`
- Shell redirection

Usage:

```bash
python3 ex2/ft_stream_management.py ancient_fragment.txt
```

Redirect normal output and errors independently:

```bash
python3 ex2/ft_stream_management.py missing.txt \
  > normal.txt 2> errors.txt
```

Provide input through a pipe:

```bash
printf 'new_archive.txt\n' | \
  python3 ex2/ft_stream_management.py ancient_fragment.txt
```

Standard file descriptors:

| Descriptor | Stream | Purpose |
|---:|---|---|
| `0` | `stdin` | Program input |
| `1` | `stdout` | Normal program output |
| `2` | `stderr` | Error output |

### ex3 - Vault Security

Introduces the `with` statement and implements `secure_archive()`, a reusable function for safe read and write operations.

Function contract:

```python
secure_archive(
    filename: str,
    operation: str = "read",
    content: str = ""
) -> tuple[bool, str]
```

The returned tuple contains:

1. A `bool` indicating success or failure.
2. A `str` containing file data, a success message, or an error message.

Main concepts:

- Context managers
- Automatic resource cleanup
- Mandatory and optional parameters
- Read and write operation selection
- Stable return contracts
- Error information returned to the caller

Usage:

```bash
python3 ex3/ft_vault_security.py
```

## Verification

Run the linter and static type checker from the project root:

```bash
flake8 ex0/ft_ancient_text.py \
  ex1/ft_archive_creation.py \
  ex2/ft_stream_management.py \
  ex3/ft_vault_security.py

mypy ex0/ft_ancient_text.py \
  ex1/ft_archive_creation.py \
  ex2/ft_stream_management.py \
  ex3/ft_vault_security.py
```

Recommended manual cases:

- Valid text file.
- Missing file.
- Inaccessible file.
- Empty destination filename.
- Existing destination file.
- Successful read and write operations.
- Invalid operation passed to `secure_archive()`.
- Permission failure during writing.

## Key takeaway

The module demonstrates the progression from manual resource management to safer, reusable file operations. Each exercise adds one layer of control: content recovery, transformation, stream separation, and automatic cleanup through context managers.

Developed as part of the 42 Barcelona curriculum.
