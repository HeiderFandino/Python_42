def secure_archive(
    filename: str,
    operation: str = "read",
    content: str = ""
) -> tuple[bool, str]:
    try:
        if operation == "read":
            with open(filename, "r") as file:
                data: str = file.read()

            return (True, data)

        if operation == "write":
            with open(filename, "w") as file:
                file.write(content)

            return (True, "Content successfully written to file")

        return (False, f"Invalid operation: {operation}")

    except OSError as error:
        return (False, f"{error}")


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    print()

    print(
        "Using 'secure_archive' to read "
        "from a nonexistent file:"
    )
    print(secure_archive("/not/existing/file"))
    print()

    print(
        "Using 'secure_archive' to read "
        "from an inaccessible file:"
    )
    print(secure_archive("/etc/master.passwd"))
    print()

    print(
        "Using 'secure_archive' to read "
        "from a regular file:"
    )
    previous_content: tuple[bool, str] = secure_archive(
        "ancient_fragment.txt"
    )
    print(previous_content)
    print()

    print(
        "Using 'secure_archive' to write "
        "previous content to a new file:"
    )

    if previous_content[0]:
        print(
            secure_archive(
                "new_archive.txt",
                "write",
                previous_content[1]
            )
        )
    else:
        print((False, "No content available to write"))
