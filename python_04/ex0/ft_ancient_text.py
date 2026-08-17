import sys
import typing


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
    else:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{sys.argv[1]}'")

        try:
            file: typing.IO[str] = open(sys.argv[1])
        except OSError as error:
            print(f"Error opening file '{sys.argv[1]}': {error}")
        else:
            content: str = file.read()
            print("---")
            print(content, end="")
            print("---")
            file.close()
            print(f"File '{sys.argv[1]}' closed.")
