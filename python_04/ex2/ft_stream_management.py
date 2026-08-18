import sys
import typing


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write(f"[STDERR] Usage: {sys.argv[0]} <file>\n")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{sys.argv[1]}'")

        try:
            file: typing.IO[str] = open(sys.argv[1])
        except OSError as error:
            sys.stderr.write(f"[STDERR] Error opening file '{sys.argv[1]}': "
                             f"{error}\n"
                             )
        else:
            content: str = file.read()
            print("---")
            print(content, end="")
            print("---")
            file.close()
            print(f"File '{sys.argv[1]}' closed.")

            lines: list[str] = content.splitlines()
            new_content: str = ""

            for line in lines:
                new_content += line + "#\n"

            print("\nTransform data:")
            print("---")
            print(new_content, end="")
            print("---")

            sys.stdout.write(
                "Enter new file name (or empty): ")
            sys.stdout.flush()

            new_file_name: str = sys.stdin.readline()
            if new_file_name.endswith("\n"):
                new_file_name = new_file_name[:-1]

            if not new_file_name:
                print("Not saving data.")
            else:
                print(f"Saving data to '{new_file_name}'")

                try:
                    new_file: typing.IO[str] = open(
                        new_file_name, "w"
                    )
                    new_file.write(new_content)
                    new_file.close()
                except OSError as error:
                    sys.stderr.write(
                        f"[STDERR] Error saving file "
                        f"'{new_file_name}': {error}\n"
                    )
                    print("Data not saved.")
                else:
                    print(
                        f"Data saved in file "
                        f"'{new_file_name}'."
                    )
