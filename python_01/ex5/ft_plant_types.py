class Plant:
    def __init__(
        self,
        name: str,
        height: int,
        days_old: int
    ) -> None:
        self.name = name
        self.height = float(height)
        self.days_old = days_old

    def grow(self) -> None:
        self.height = round(self.height + 2.1, 1)

    def age(self) -> None:
        self.days_old += 1

    def show(self) -> None:
        print(
            f"{self.name}: {self.height}cm, "
            f"{self.days_old} days old"
        )


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        days_old: int,
        color: str
    ) -> None:
        super().__init__(name, height, days_old)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        self.is_blooming = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")

        if self.is_blooming:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        days_old: int,
        trunk_diameter: int
    ) -> None:
        super().__init__(name, height, days_old)
        self.trunk_diameter = float(trunk_diameter)

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.height}cm long and "
            f"{self.trunk_diameter}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        days_old: int,
        harvest_season: str,
        nutritional_value: int
    ) -> None:
        super().__init__(name, height, days_old)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":
    rose = Flower("Rose", 15, 10, "red")
    oak = Tree("Oak", 200, 365, 5)
    tomato = Vegetable("Tomato", 5, 10, "April", 0)

    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print()

    print("=== Tree")
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print()

    print("=== Vegetable")
    tomato.show()
    print("[make tomato grow and age for 20 days]")

    for _ in range(20):
        tomato.grow()
        tomato.age()

    tomato.show()
