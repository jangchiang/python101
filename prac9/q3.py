def main():
    choice = str(input("Do you want black or white coffee?: ")).upper()
    size = str(input("choose size: ")).upper()
    price = condition(choice, size)
    print(f"you choose {choice} and {size} size. you need to pay: {price}")


def condition(choice, size):
    if choice == 'BLACK':
        if size == 'SMALL':
            price = 3
        elif size == 'MEDIUM':
            price = 4
        else:
            price = 5
    else:
        if size == 'SMALL':
            price = 4
        elif size == 'MEDIUM':
            price = 5
        else:
            price = 6
    return price


main()
