#error Checking
while True:
    lv = int(input("please get level: "))
    if lv in range(1, 7):
        print("level: ", lv, " select", sep="")
        break
    else:
        print("invalid number")

