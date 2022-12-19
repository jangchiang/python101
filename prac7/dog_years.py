def main():
    human_age = get_human_age()
    dog_age = calculate_dog_year(human_age)
    display(dog_age)


def get_human_age():
    hage = int(input("Enter human years: "))
    return hage


def calculate_dog_year(hage):
    if hage <= 2:
        dage = hage * 10.5
    else:
        dage = 21 + 4 * (hage - 2)
    return dage


def display(dage):
    print(f"This dog is {dage} years old")


main()
