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
                self._data.append(
                    (self._next_rank, str(item))
                )
                self._next_rank += 1
        else:
            self._data.append(
                (self._next_rank, str(data))
            )
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

    def ingest(
        self,
        data: str | list[str]
    ) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        if isinstance(data, str):
            self._data.append(
                (self._next_rank, data)
            )
            self._next_rank += 1
        else:
            for item in data:
                self._data.append(
                    (self._next_rank, item)
                )
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
            self._data.append(
                (self._next_rank, log_str)
            )
            self._next_rank += 1
        else:
            for item in data:
                log_str = ": ".join(item.values())
                self._data.append(
                    (self._next_rank, log_str)
                )
                self._next_rank += 1


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(
        self,
        proc: DataProcessor
    ) -> None:
        self._processors.append(proc)

    def process_stream(
        self,
        stream: list[Any]
    ) -> None:
        for element in stream:
            processed = False

            for processor in self._processors:
                if processor.validate(element):
                    processor.ingest(element)
                    processed = True
                    break

            if not processed:
                print(
                    "DataStream error - "
                    f"Can't process element in stream: {element}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")

        if not self._processors:
            print("No processor found, no data")
            return

        for processor in self._processors:
            name = processor.__class__.__name__
            name = name.replace("Processor", " Processor")

            print(
                f"{name}: total "
                f"{processor._next_rank} items processed, "
                f"remaining {len(processor._data)} "
                "on processor"
            )


def main() -> None:
    print("=== Code Nexus - Data Stream ===")
    print()
    print("Initialize Data Stream...")

    data_stream = DataStream()

    data_stream.print_processors_stats()
    print()

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    print("Registering Numeric Processor")
    print()
    data_stream.register_processor(numeric)

    stream: list[Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected",
            },
        ],
        42,
        ["Hi", "five"],
    ]

    print(f"Send first batch of data on stream: {stream}")
    data_stream.process_stream(stream)

    data_stream.print_processors_stats()
    print()

    print("Registering other data processors")
    data_stream.register_processor(text)
    data_stream.register_processor(log)

    print("Send the same batch again")
    data_stream.process_stream(stream)

    data_stream.print_processors_stats()
    print()

    print(
        "Consume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )

    numeric.output()
    numeric.output()
    numeric.output()

    text.output()
    text.output()

    log.output()

    data_stream.print_processors_stats()


if __name__ == "__main__":
    main()
