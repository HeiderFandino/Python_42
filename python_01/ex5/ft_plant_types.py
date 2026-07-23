class Plant:
    def __init__(self, name: str, height: int, age_days: int) -> None:
        self.name = name
        self._height = float(height)
        self._age_days = age_days

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age_days} days old")


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age_days: int,
        color: str
    ) -> None:
        super().__init__(name, height, age_days)
        self.color = color

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")

    rose = Flower("Rose", 15, 10, "red")
    rose.show()
