class Plant:
    name: str
    height: int
    age: int

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25
    rose.age = 30

    sunflower = Plant()
    sunflower.name = "Sunflower"
    sunflower.height = 25
    sunflower.age = 30

    cactus = Plant()
    cactus.name = "Cactus"
    cactus.height = 25
    cactus.age = 30

    print("=== Garden Plant Registry ===")
    rose.show()
    sunflower.show()
    cactus.show()
"""class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age        
    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} daysold")

if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    rose.show()
    sunflower.show()
    cactus.show()"""
