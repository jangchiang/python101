"""func2"""
import random


def main():
    namelist = []
    name_check(namelist)
    for i in range(len(namelist)):
        print(f"Hi {namelist[i]} from {birthplace()}")
        i += 1


def name_check(namelist):
    while True:
        name = str(input("Enter your name please: "))
        if name == "":
            break
        else:
            namelist.append(name)


""""make more challenge Do the birthplace to RNG"""


def birthplace():
    place = ['Thailand', 'Japan', 'UK', 'Singapore', 'USA', 'Russia', 'Korea', 'New Zealand']
    country = random.choice(place)  # choice is random the element from given sequence
    return country


main()
