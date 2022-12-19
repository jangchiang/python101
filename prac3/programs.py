# 1. tax
print("Python party tax program - where tax is a party", sep="")
income = float(input("get your income: $"))
if income < 100:
    print("you don't pay any tax", sep="")
elif income > 1000:
    tax = income*0.10
    pb = income-tax
    print("total tax is: $", "%.2f"%tax, sep="")
    print("take home pay is: $", "%.2f"%pb, sep="")
else:
    tax = income*0.05
    pb = income-tax
    print("total tax is: $", "%.2f"%tax, sep="")
    print("take home pay is: $", "%.2f"%pb, sep="")


# 2. Car Insurance
print("car Insurance")
age = int(input("please input you age: "))
if age < 0:
    print("age must be positive number", sep="")
elif age < 18:
    print("Hire refuced", sep="")
elif age <25:
    print("Insurance required", sep="")
else:
    print("Insurance not require", sep="")

    
# 3. Simple Password Checker
print("secret password checker", sep="")
pws = input("please get your password in here:")
key = str("chiang2078")
if pws == key:
    print("access granted", sep="")
else:
    print("access denied", sep="")


# 4. Dog Years
h_age = int(input("get human age: "))
if h_age < 0:
    print("age must be positive number")
elif h_age <= 2:
    d_age = h_age * 10.5
else:
    d_age = 21+(h_age-2) * 4
print("age in dog year is: ", d_age, sep="")


# 5. Rock of Ages
age: int = int(input("get your age please:"))
if 0 <= age <= 5:
    print('you age is ', age, ". ", " you are baby, pls call me uncle", sep="")
elif 6 < age <= 10:
    print("you age is ", age, ". ", "Handsome boy, you are child.", sep="")
elif 10 < age <= 18:
    print("you age is ", age, ". ", "Just a teens~~ just do it you have a fire!!!!", sep="")
elif 18 < age <= 30:
    print("you age is ", age, ". ", "try to should your way.", sep="")
elif 30 < age <= 50:
    print("you age is ", age, ". ", "work hard do harder make more money~~", sep="")
elif 50 < age <= 75:
    print("you age is ", age, ". ", "time to retired", sep="")
elif 75 < age <= 120:
    print("you age is ", age, ". ", "Are you serious? Are you ancient man?", sep="")
else:
    print("Invaild age", sep="")


# 6. Speeding Fines
s = float(input("please enter your speed (km/h):"))
sl = float(input("please enter the speed limit(km/h):"))
d = s-sl
if 0< d <=13:
    pa = 177
    dp = 1
    print("your speed is: ", "%.2f" % s, " km/h", sep="")
    print("your penalty amount is: $", pa, sep="")
    print("your demerit points is ", dp, sep="")
elif 13 < d <=20:
    pa = 266
    dp = 3
    print("your speed is: ", "%.2f" % s, " km/h", sep="")
    print("your penalty amount is: $", pa, sep="")
    print("your demerit points is ", dp, sep="")
elif 20 < d <= 30:
    pa = 444
    dp = 4
    print("your speed is: ", "%.2f" % s, " km/h", sep="")
    print("your penalty amount is: $", pa, sep="")
    print("your demerit points is ", dp, sep="")
elif 30 < d <= 40:
    pa = 622
    dp = 6
    print("your speed is: ", "%.2f" % s, " km/h", sep="")
    print("your penalty amount is: $", pa, sep="")
    print("your demerit points is ", dp, sep="")
elif d > 40:
    pa = 1245
    dp = 8
    print("your speed is: ", "%.2f" % s, " km/h", sep="")
    print("your penalty amount is: $", pa, sep="")
    print("your demerit points is ", dp, sep="")
else:
    print("you don't have any fines")