class Plant:
    def __init__(
        self,
        name: str,
        starting_height: int,
        starting_age: int
    ) -> None:
        self.name = name
        self.starting_height = float(starting_height)
        self.starting_age = starting_age

    def show(self) -> None:
        print(
            f"Created: {self.name}: {self.starting_height}cm, "
            f"{self.starting_age} days old"
        )


if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 200, 365)
    cactus = Plant("Cactus", 5, 90)
    sunflower = Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 120)

    rose.show()
    oak.show()
    cactus.show()
    sunflower.show()
    fern.show()
