"""4. Add Functions to Previous Pracs"""

def kmtoMiles(x):
    km = 0.621371
    mile = x * km
    return mile

def main():
    while True:
        x = float(input("Enter distance in kilometres: "))
        print(f"{x} is {kmtoMiles(x):.2f} miles")
main()