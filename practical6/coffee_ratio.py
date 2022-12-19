"""1. Coffee Brew Ratio"""


def get_coffee_style(ratio):
    if ratio < 2:
        style = "ristretto"
    elif ratio < 3:
        style = "normale"
    else:
        style = "lungo"
    return style


def main():
    d = float(input("get coffee dose: "))
    y = float(input("get yield: "))
    ratio = y / d
    style = get_coffee_style(ratio)
    print(f"1 : {ratio:.1f} is considered {style}")


main()
