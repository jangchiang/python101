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
