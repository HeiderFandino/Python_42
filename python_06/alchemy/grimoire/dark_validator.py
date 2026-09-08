from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed_ingredients: list[str] = dark_spell_allowed_ingredients()
    lower_ingredients: str = ingredients.lower()

    for ingredient in allowed_ingredients:
        if ingredient in lower_ingredients:
            return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"
