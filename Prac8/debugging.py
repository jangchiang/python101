# Debug program 1 - friends' names
"""
1- friends' names

names = ["Abby", "Jerome", "Olivia", "Monique"]
print("My friends' names: ")
for i in range(1, len(names)):
    print(f"{i}. {names[i]}")
last_number = len(names)
print(f"The last name is {names[last_number]}")
_______________~explain and fixed~____________________________
problem explain:
line9: range error
line8: When comparing in the number format, the program will process 0, 1, 2, 3, making the complete list not visible.
fixed:
line7: +1 after len(name)
line8: to show Abby need to add i-1 in names[i]
_______________________________________________________________
"""
names = ["Abby", "Jerome", "Olivia", "Monique"]
print("My friends' names: ")
for i in range(1, len(names)+1):
    print(f"{i}. {names[i-1]}")
last_number = len(names)-1
print(f"The last name is {names[last_number]}")


# Debug program 2 - title-casing country names
"""
countries = ("australia", "new zeaLAND", "USA")
for i in range(len(countries)):
    countries[i] = countries[i].title()

_________________~explain and fixed~________________________
problem explain:
no output
line31: the variable error
fixed:
change line38: from countries[i] = countries[i].title()
                to  country = countries[i].title()
____________________________________________________________
"""
countries = ("australia", "new zeaLAND", "USA")
for i in range(len(countries)):
    country = countries[i].title()
    print(country)
