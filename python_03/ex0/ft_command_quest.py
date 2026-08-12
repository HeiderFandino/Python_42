import sys


def command_quest() -> None:

    if len(sys.argv) == 1:
        print("=== Command Quest ===")
        print("Program name:", sys.argv[0])
        print("No arguments provided!")
        print("Total arguments:", len(sys.argv))
    else:
        print("=== Command Quest ===")
        print("Program name:", sys.argv[0])
        print("Arguments received:", len(sys.argv[1:]))
        i = 1
        for argv in sys.argv[1:]:
            print(f"Argument {i}: {argv}")
            i += 1
        print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    command_quest()
