from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[tuple[int, str]] = []
        self._next_rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    @abstractmethod
    def ingest(self, data: Any) -> None:
        ...

    def output(self) -> tuple[int, str]:
        return self._data.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return (
            (
                isinstance(data, int | float)
                and not isinstance(data, bool)
            )
            or (
                isinstance(data, list)
                and all(
                    isinstance(item, int | float)
                    and not isinstance(item, bool)
                    for item in data
                )
            )
        )

    def ingest(
        self,
        data: int | float | list[int | float]
    ) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, list):
            for item in data:
                item_str = str(item)
                self._data.append((self._next_rank, item_str))
                self._next_rank += 1
        else:
            item_str = str(data)
            self._data.append((self._next_rank, item_str))
            self._next_rank += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return (
            isinstance(data, str)
            or (
                isinstance(data, list)
                and all(
                    isinstance(item, str)
                    for item in data
                )
            )
        )

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        if isinstance(data, str):
            self._data.append((self._next_rank, data))
            self._next_rank += 1
        else:
            for item in data:
                self._data.append((self._next_rank, item))
                self._next_rank += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return (
            (
                isinstance(data, dict)
                and all(
                    isinstance(key, str)
                    and isinstance(value, str)
                    for key, value in data.items()
                )
            )
            or (
                isinstance(data, list)
                and all(
                    isinstance(item, dict)
                    and all(
                        isinstance(key, str)
                        and isinstance(value, str)
                        for key, value in item.items()
                    )
                    for item in data
                )
            )
        )

    def ingest(
        self,
        data: dict[str, str] | list[dict[str, str]]
    ) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        if isinstance(data, dict):
            log_str = ": ".join(data.values())
            self._data.append((self._next_rank, log_str))
            self._next_rank += 1
        else:
            for item in data:
                log_str = ": ".join(item.values())
                self._data.append((self._next_rank, log_str))
                self._next_rank += 1

def main() -> None:
    print("=== Code Nexus - Data Processor ===")

    print("\nTesting Numeric Processor...")
    numeric_processor = NumericProcessor()

    print(
        " Trying to validate input '42': "
        f"{numeric_processor.validate(42)}"
    )
    print(
        " Trying to validate input 'Hello': "
        f"{numeric_processor.validate('Hello')}"
    )

    print(
        " Test invalid ingestion of string 'foo' "
        "without prior validation:"
    )
    try:
        numeric_processor.ingest("foo")
    except ValueError as error:
        print(f" Got exception: {error}")

    numeric_data = [1, 2, 3, 4, 5]
    print(f" Processing data: {numeric_data}")
    numeric_processor.ingest(numeric_data)

    print(" Extracting 3 values...")
    for _ in range(3):
        rank, value = numeric_processor.output()
        print(f" Numeric value {rank}: {value}")

    print("\nTesting Text Processor...")
    text_processor = TextProcessor()

    print(
        " Trying to validate input '42': "
        f"{text_processor.validate(42)}"
    )

    text_data = ["Hello", "Nexus", "World"]
    print(f" Processing data: {text_data}")
    text_processor.ingest(text_data)

    print(" Extracting 1 value...")
    rank, value = text_processor.output()
    print(f" Text value {rank}: {value}")

    print("\nTesting Log Processor...")
    log_processor = LogProcessor()

    print(
        " Trying to validate input 'Hello': "
        f"{log_processor.validate('Hello')}"
    )

    log_data = [
        {
            "log_level": "NOTICE",
            "log_message": "Connection to server",
        },
        {
            "log_level": "ERROR",
            "log_message": "Unauthorized access!!",
        },
    ]

    print(f" Processing data: {log_data}")
    log_processor.ingest(log_data)

    print(" Extracting 2 values...")
    for _ in range(2):
        rank, value = log_processor.output()
        print(f" Log entry {rank}: {value}")


if __name__ == "__main__":
    main()
