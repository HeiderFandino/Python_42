import sys


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")

    inventory: dict[str, int] = {}

    for argument in sys.argv[1:]:
        parts = argument.split(":")

        if len(parts) != 2:
            print(f"Error - invalid parameter '{argument}'")
            continue

        item, quantity_text = parts

        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue

        try:
            quantity = int(quantity_text)
        except ValueError as error:
            print(f"Quantity error for '{item}': {error}")
            continue

        inventory[item] = quantity

    item_list: list[str] = list(inventory.keys())
    total_items: int = len(item_list)
    total_quantity: int = sum(inventory.values())

    print("Got inventory:", inventory)
    print("Item list:", item_list)
    print(
        f"Total quantity of the {total_items} items: "
        f"{total_quantity}"
    )

    if total_quantity != 0:
        for item in inventory:
            item_quantity = inventory[item]
            percentage = round(
                (item_quantity / total_quantity) * 100,
                1,
            )
            print(f"Item {item} represents {percentage}%")

    if len(item_list) > 0:
        most_abundant = item_list[0]
        least_abundant = item_list[0]

        for item in inventory:
            if inventory[item] > inventory[most_abundant]:
                most_abundant = item

            if inventory[item] < inventory[least_abundant]:
                least_abundant = item

        print(
            f"Item most abundant: {most_abundant} "
            f"with quantity {inventory[most_abundant]}"
        )
        print(
            f"Item least abundant: {least_abundant} "
            f"with quantity {inventory[least_abundant]}"
        )

    inventory.update({"magic_item": 1})
    print("Updated inventory:", inventory)
