print("car Insurance")
age = int(input("please input you age: "))
if age < 0:
    print("age must be positive number")
elif age < 18:
    print("Hire refuced")
elif age <25:
    print("Insurance required")
else:
    print("Insurance not require")