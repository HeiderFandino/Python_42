def light_spell_allowed_ingredients() -> list[str]:
    allowed_ingredients: list[str] = ["earth", "air", "fire", "water"]
    return allowed_ingredients


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients

    validation: str = validate_ingredients(ingredients)

    if validation.endswith(" - VALID"):
        return f"Spell recorded: {spell_name} ({validation})"

    return f"Spell rejected: {spell_name} ({validation})"
