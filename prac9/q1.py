def calculate(original, change):
    result = original + (original * change)
    print(f"Original is {original}, Change is {change}, result is {result}")


def main():
    original = float(input("please get the original price: "))
    change = float(input("Enter change: "))
    calculate(original, change)


main()