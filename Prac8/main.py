def menu():
    print("Menu:")
    print("(I)nstruction")
    print("(C)alculate")
    print("(Q)uit")
    choice = str(input("Choice: ")).upper()
    return choice


def FaQ():
    print("Enter the number of products you want to buy and your chosen price. If you buy 0-5 items, they're full price, over 5 items and each one is 10% off!")


def calculate():
    while True:
        n = int(input("number of product: "))
        if 0 <= n <= 5:
            p = float(input("price: "))
            total = n * p
            print(f"{n} x % {p} products cost = % {total:.2f}", sep="")
            break
        elif n > 5:
            p = float(input("price: "))
            dc = (n * p) * 0.1
            total = (n * p) - dc
            print(f"{n} x % {p} products cost = % {total:.2f}", sep="")
            break
        else:
            print("the number of product must be positive")


def main():
    choice = menu()
    while choice != 'Q':
        if choice =='I':
            FaQ()
        elif choice == 'C':
            calculate()
        else:
            print("Invalid choice")
        choice = menu()
    print("End of program")


main()