import sys


def command_quest() -> None:
    if len(sys.argv) == 1:
        print("=== Command Quest ===")
        print(f"Program name: {sys.argv[0]}")
        print("No arguments provided!")
        print("Total arguments:", len(sys.argv))
    else:
        argc = len(sys.argv)
        print("=== Command Quest ===")
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {argc - 1}")
        i = 1
        for argument in sys.argv[1:]:
            print(f"Argument {i}: {argument}")
            i += 1
        print("Total arguments:", len(sys.argv))


if __name__ == "__main__":
    command_quest()
