h_age = int(input("get human age: "))
if h_age < 0:
    print("age must be positive number")
elif h_age <= 2:
    d_age = h_age * 10.5
else:
    d_age = 21+(h_age-2) * 4
print("age in dog year is: ", d_age, sep="")