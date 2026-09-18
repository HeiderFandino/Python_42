from ex0.creature import Creature, CreatureFactory
from .capabilities import TransformCapability


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")
        self.is_transformed = False

    def attack(self) -> str:
        if not self.is_transformed:
            return (f"{self.name} attacks normally.")
        else:
            return (f"{self.name} performs a boosted strike!")

    def transform(self) -> str:
        self.is_transformed = True
        return (f"{self.name} shifts into a sharper form!")

    def revert(self) -> str:
        self.is_transformed = False
        return (f"{self.name} returns to normal.")


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal/Dragon")
        self.is_transformed = False

    def attack(self) -> str:
        if not self.is_transformed:
            return f"{self.name} attacks normally."
        else:
            return f"{self.name} unleashes a devastating morph strike!"

    def transform(self) -> str:
        self.is_transformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.is_transformed = False
        return f"{self.name} stabilizes its form."


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        creature = Shiftling()
        return creature

    def create_evolved(self) -> Morphagon:
        creature_evolved = Morphagon()
        return creature_evolved
