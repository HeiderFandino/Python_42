import sys
import typing


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
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

            lines: list[str] = content.splitlines()
            new_content: str = ""

            for line in lines:
                new_content += line + "#\n"

            print("\nTransform data:")
            print("---")
            print(new_content, end="")
            print("---")

            new_file_name: str = input(
                "Enter new file name (or empty): "
            )

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
                    print(
                        f"Error saving file "
                        f"'{new_file_name}': {error}"
                    )
                else:
                    print(
                        f"Data saved in file "
                        f"'{new_file_name}'."
                    )
