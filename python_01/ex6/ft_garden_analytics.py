class Plant:
    class Statistics:
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def record_grow(self) -> None:
            self._grow_count += 1

        def record_age(self) -> None:
            self._age_count += 1

        def record_show(self) -> None:
            self._show_count += 1

        def display(self) -> None:
            print(
                f"Stats: {self._grow_count} grow, "
                f"{self._age_count} age, "
                f"{self._show_count} show"
            )

    def __init__(
        self,
        name: str,
        height: int,
        days_old: int
    ) -> None:
        self.name = name
        self.height = float(height)
        self.days_old = days_old
        self.statistics = self.Statistics()

    def grow(self) -> None:
        self.height = round(self.height + 2.1, 1)
        self.statistics.record_grow()

    def age(self) -> None:
        self.days_old += 1
        self.statistics.record_age()

    def show(self) -> None:
        self.statistics.record_show()
        print(
            f"{self.name}: {self.height}cm, "
            f"{self.days_old} days old"
        )

    @staticmethod
    def is_older_than_year(days_old: int) -> bool:
        return days_old > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0, 0)


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

    def grow(self) -> None:
        self.height = round(self.height + 8.0, 1)
        self.statistics.record_grow()

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
    class Statistics(Plant.Statistics):
        def __init__(self) -> None:
            super().__init__()
            self._shade_count = 0

        def record_shade(self) -> None:
            self._shade_count += 1

        def display(self) -> None:
            super().display()
            print(f" {self._shade_count} shade")

    def __init__(
        self,
        name: str,
        height: int,
        days_old: int,
        trunk_diameter: int
    ) -> None:
        super().__init__(name, height, days_old)
        self.statistics: Tree.Statistics = Tree.Statistics()
        self.trunk_diameter = float(trunk_diameter)

    def produce_shade(self) -> None:
        self.statistics.record_shade()
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

    def age(self) -> None:
        super().age()
        self.nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: int,
        days_old: int,
        color: str
    ) -> None:
        super().__init__(name, height, days_old, color)
        self.seeds = 0

    def grow(self) -> None:
        self.height = round(self.height + 30.0, 1)
        self.statistics.record_grow()

    def age(self) -> None:
        self.days_old += 20
        self.statistics.record_age()

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seeds}")


def display_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.statistics.display()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(
        "Is 30 days more than a year? -> "
        f"{Plant.is_older_than_year(30)}"
    )
    print(
        "Is 400 days more than a year? -> "
        f"{Plant.is_older_than_year(400)}"
    )
    print()

    print("=== Flower")
    rose = Flower("Rose", 15, 10, "red")
    rose.show()
    display_statistics(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_statistics(rose)
    print()

    print("=== Tree")
    oak = Tree("Oak", 200, 365, 5)
    oak.show()
    display_statistics(oak)

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_statistics(oak)
    print()

    print("=== Seed")
    sunflower = Seed("Sunflower", 80, 45, "yellow")
    sunflower.show()

    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    display_statistics(sunflower)
    print()

    print("=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    display_statistics(anonymous)
