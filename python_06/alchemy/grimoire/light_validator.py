from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    list_allowed_ingredients: list[str] = light_spell_allowed_ingredients()
    lower_ingredients: str = ingredients.lower()
    for ingredient in list_allowed_ingredients:
        if ingredient in lower_ingredients:
            return (f"{ingredients} - VALID")
    return f"{ingredients} - INVALID"
