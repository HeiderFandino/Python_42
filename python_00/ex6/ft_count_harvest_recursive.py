def ft_harvest_recursive(day, days):
    if day > days:
        return

    print("Day", day)
    ft_harvest_recursive(day + 1, days)


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    ft_harvest_recursive(1, days)
    print("Harvest time!")
