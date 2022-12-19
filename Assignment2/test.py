# CP1401 Assignment 2
"""
Plan:

"""


def main():
    titlelist = []
    pricelist = []
    print("Welcome to the Movie App!")
    print("Written by Theeradon Somsri")
    while True:
        choice = menu()
        if choice == 'I':
            info()
        elif choice == 'A':
            add_movie(titlelist, pricelist)
        elif choice == 'R':
            remove_movie(titlelist, pricelist)
            displaylist(titlelist, pricelist)
        elif choice == 'B':
            buy_ticket(titlelist, pricelist)
        elif choice == 'S':
            displaylist(titlelist, pricelist)
        elif choice == 'Q':
            print("Farewell and thank you for using this movie app.")
            displaylist(titlelist, pricelist)
            break
        else:
            print(f"Invalid menu choice.\n")


def menu():
    print("Menu")
    print("(I)nformation")
    print("(A)dd Movie")
    print("(R)emove Movie")
    print("(B)uy Ticket")
    print("(S)how List of Movies")
    print("(Q)uit")
    choice = str(input("Enter your choice: ")).upper()
    return choice


def info():
    print(f"This is a simple movie application program. It allows user to display information about the program, "
          "add new movie to the selection, remove a movie, help customer buy ticket to watch a movie, and computing "
          "the total cost for tickets. When (Q)uit is selected, the program will display the list of movies and their "
          "respective ticket prices.\n", sep="")


def add_movie(titlelist, pricelist):
    while True:
        title = str(input("Enter the movie title: ")).upper()
        if title in titlelist:
            print(f"This movie is already in the collection!\n")
            break
        else:
            titlelist.append(title)
            price = float(input("enter ticket price: "))
            while price < 0:
                print("ticket price cannot be negative")
                price = float(input("enter ticket price: "))
            pricelist.append(price)
            print(f"the new movie title added: {title}, ${price}\n")
            break


def displaylist(titlelist, pricelist):
    print("List of Movies Currently Available:")
    if len(titlelist) == 0:
        print(f"No movie available.\n")
    else:
        print(f"No.\t\tname\t\t\t\t\t\t\tprice")
        for i in range(len(titlelist)):
            print(f"{i + 1}.\t\t{titlelist[i]}\t\t\t\t\t\t\t${pricelist[i]}")
            i += 1


def remove_movie(titlelist, pricelist):
    while True:
        remove = str(input("Enter title movie which you want to remove: ")).upper()
        confirm = str(input(f"ARE YOU SURE TO REMOVE(\'yes\' to remove): ")).lower()
        if remove in titlelist:
            if confirm == 'yes':
                x = titlelist.index(remove)
                pricelist.pop(x)
                titlelist.remove(remove)
                print("the movie removed\n")
                break
            else:
                print(f"back to the program\n")
        else:
            print(f"Error: no such movie!\n")


def buy_ticket(titlelist, pricelist):
    while True:
        name = str(input("Enter customer name>"))
        if name == "":
            print("Error: please enter your name")
        else:
            displaylist(titlelist, pricelist)
            while True:
                num = int(input(f"{name}, Please enter movie number: "))
                if num > 0:
                    if num < len(titlelist)+1:
                        adult = int(input(f"{name}, please enter number of adult tickets needed: "))
                        child = int(input(f"{name}, please enter number of child tickets needed: "))
                        print(f"Thank you, {name}. Your receipt is:")
                        num -= 1
                        price = pricelist[num]
                        ap = adult * price
                        discount = price * 0.5
                        cp = child * discount
                        total = ap + cp
                        print(f"Movie title:\t{titlelist[num]}")
                        print(f"product\t\t\tunit\t\t\tprice/unit\t\t\ttotal")
                        print(f"Adults:\t\t\t{adult}\t\t\t\t{price}\t\t\t\t{ap}")
                        print(f"Child:\t\t\t{child}\t\t\t\t{discount}\t\t\t\t{cp}")
                        print(f"Please pay: {total}")
                        print("Enjoy with the show.\n")
                        break
                    else:
                        print("Error:the number of movie with you find is not true")
                        displaylist(titlelist, pricelist)
                else:
                    print("Error: number cannot be negative!")
                    displaylist(titlelist, pricelist)


main()
