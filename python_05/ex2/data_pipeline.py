from abc import ABC, abstractmethod
from typing import Any, Protocol


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
            log_string = ": ".join(data.values())
            self._data.append(
                (self._next_rank, log_string)
            )
            self._next_rank += 1
        else:
            for item in data:
                log_string = ": ".join(item.values())
                self._data.append(
                    (self._next_rank, log_string)
                )
                self._next_rank += 1


class ExportPlugin(Protocol):
    def process_output(
        self,
        data: list[tuple[int, str]]
    ) -> None:
        ...


class CSVExportPlugin:
    def process_output(
        self,
        data: list[tuple[int, str]]
    ) -> None:
        values: list[str] = []

        for _, value in data:
            values.append(self._escape_csv(value))

        print("CSV Output:")
        print(",".join(values))

    def _escape_csv(self, value: str) -> str:
        must_quote = (
            "," in value
            or '"' in value
            or "\n" in value
            or "\r" in value
        )

        if not must_quote:
            return value

        escaped_value = value.replace('"', '""')
        return f'"{escaped_value}"'


class JSONExportPlugin:
    def process_output(
        self,
        data: list[tuple[int, str]]
    ) -> None:
        entries: list[str] = []

        for rank, value in data:
            key = f"item_{rank}"
            escaped_key = self._escape_json(key)
            escaped_value = self._escape_json(value)

            entries.append(
                f'"{escaped_key}": "{escaped_value}"'
            )

        print("JSON Output:")
        print("{" + ", ".join(entries) + "}")

    def _escape_json(self, value: str) -> str:
        escaped: list[str] = []

        for character in value:
            if character == '"':
                escaped.append('\\"')
            elif character == "\\":
                escaped.append("\\\\")
            elif character == "\b":
                escaped.append("\\b")
            elif character == "\f":
                escaped.append("\\f")
            elif character == "\n":
                escaped.append("\\n")
            elif character == "\r":
                escaped.append("\\r")
            elif character == "\t":
                escaped.append("\\t")
            elif ord(character) < 32:
                escaped.append(
                    f"\\u{ord(character):04x}"
                )
            else:
                escaped.append(character)

        return "".join(escaped)


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

    def output_pipeline(
        self,
        nb: int,
        plugin: ExportPlugin
    ) -> None:
        if nb < 0:
            raise ValueError(
                "The number of elements cannot be negative"
            )

        for processor in self._processors:
            output_data: list[tuple[int, str]] = []

            amount = min(nb, len(processor._data))

            for _ in range(amount):
                output_data.append(processor.output())

            plugin.process_output(output_data)


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===")
    print()
    print("Initialize Data Stream...")
    print()

    data_stream = DataStream()
    data_stream.print_processors_stats()
    print()

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    print("Registering Processors")
    print()

    data_stream.register_processor(numeric)
    data_stream.register_processor(text)
    data_stream.register_processor(log)

    first_stream: list[Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": (
                    "Telnet access! Use ssh instead"
                ),
            },
            {
                "log_level": "INFO",
                "log_message": (
                    "User wil is connected"
                ),
            },
        ],
        42,
        ["Hi", "five"],
    ]

    print(
        "Send first batch of data on stream: "
        f"{first_stream}"
    )
    print()

    data_stream.process_stream(first_stream)
    data_stream.print_processors_stats()
    print()

    csv_plugin = CSVExportPlugin()

    print(
        "Send 3 processed data from each "
        "processor to a CSV plugin:"
    )
    data_stream.output_pipeline(3, csv_plugin)
    print()

    data_stream.print_processors_stats()
    print()

    second_stream: list[Any] = [
        21,
        [
            "I love AI",
            "LLMs are wonderful",
            "Stay healthy",
        ],
        [
            {
                "log_level": "ERROR",
                "log_message": "500 server crash",
            },
            {
                "log_level": "NOTICE",
                "log_message": (
                    "Certificate expires in 10 days"
                ),
            },
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]

    print(
        "Send another batch of data: "
        f"{second_stream}"
    )
    print()

    data_stream.process_stream(second_stream)
    data_stream.print_processors_stats()
    print()

    json_plugin = JSONExportPlugin()

    print(
        "Send 5 processed data from each "
        "processor to a JSON plugin:"
    )
    data_stream.output_pipeline(5, json_plugin)
    print()

    data_stream.print_processors_stats()


if __name__ == "__main__":
    main()
