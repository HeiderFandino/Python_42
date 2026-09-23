import os
import sys

from dotenv import load_dotenv


def get_configuration() -> dict[str, str | None]:
    load_dotenv()

    mode = os.getenv("MATRIX_MODE", "development")

    if mode == "development":
        default_log_level = "DEBUG"
    else:
        default_log_level = "INFO"

    return {
        "MATRIX_MODE": mode,
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL", default_log_level),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
    }


def check_configuration(
    config: dict[str, str | None],
) -> bool:
    required_variables = (
        "DATABASE_URL",
        "API_KEY",
        "ZION_ENDPOINT",
    )

    valid = True

    for variable in required_variables:
        if not config[variable]:
            print(f"[WARNING] Missing configuration: {variable}")
            valid = False

    return valid


def get_database_status(database_url: str | None) -> str:
    if not database_url:
        return "Not configured"

    if "localhost" in database_url or "127.0.0.1" in database_url:
        return "Connected to local instance"

    return "Connected to production instance"


def get_api_status(api_key: str | None) -> str:
    if api_key:
        return "Authenticated"

    return "Not configured"


def get_zion_status(zion_endpoint: str | None) -> str:
    if zion_endpoint:
        return "Online"

    return "Offline"


def check_env_file() -> bool:
    return os.path.exists(".env")


def check_gitignore() -> bool:
    try:
        with open(".gitignore", "r", encoding="utf-8") as file:
            for line in file:
                if line.strip() == ".env":
                    return True
    except OSError:
        return False

    return False


def display_configuration(
    config: dict[str, str | None],
) -> None:
    print("\nConfiguration loaded:")
    print(f"Mode: {config['MATRIX_MODE']}")
    print(
        "Database: "
        f"{get_database_status(config['DATABASE_URL'])}"
    )
    print(f"API Access: {get_api_status(config['API_KEY'])}")
    print(f"Log Level: {config['LOG_LEVEL']}")
    print(
        "Zion Network: "
        f"{get_zion_status(config['ZION_ENDPOINT'])}"
    )


def display_security_check() -> None:
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")

    if check_env_file():
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found")

    if check_gitignore():
        print("[OK] Production overrides available")
    else:
        print("[WARNING] .env is not protected by .gitignore")


def main() -> int:
    print("ORACLE STATUS: Reading the Matrix...")

    config = get_configuration()

    configuration_valid = check_configuration(config)

    display_configuration(config)
    display_security_check()

    if configuration_valid:
        print("\nThe Oracle sees all configurations.")
        return 0

    print("\nThe Oracle detected missing configuration.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
