import alchemy.elements
from ..potions import strength_potion
import elements


def lead_to_gold() -> str:
    return (
            f"Recipe transmuting Lead to Gold: brew '"
            f"{alchemy.elements.create_air()}' "
            f"and '{strength_potion()}' mixed with '{elements.create_fire()}'"
    )
