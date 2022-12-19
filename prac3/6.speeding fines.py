s=0
sl=0
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
