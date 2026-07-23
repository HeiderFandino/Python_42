class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = 0.0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, new_height: float) -> None:
        if new_height >= 0:
            self._height = float(new_height)
        else:
            print(f"{self.name}: Error, height can't be negative")

    def set_age(self, new_age: int) -> None:
        if new_age >= 0:
            self._age = new_age
        else:
            print(f"{self.name}: Error, age can't be negative")

    def show(self) -> None:
        print(
            f"{self.name}: {self.get_height()}cm, "
            f"{self.get_age()} days old"
        )


if __name__ == "__main__":
    print("=== Garden Security System ===")

    rose = Plant("Rose", 15, 10)
    rose.show()

    print("\nProbando con valores correctos:")
    rose.set_height(25)
    rose.set_age(30)
    rose.show()

    print("\nProbando con valores negativos:")
    rose.set_height(-5)
    rose.set_age(-10)

    print("\nFinal state:")
    rose.show()
    rose.show()
