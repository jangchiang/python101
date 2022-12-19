#error Checking
lv = int(input("please get your worker level: "))
while True:
    if lv in range(1, 11):
        sl = lv * 5000
        print("your worker is: ", lv, " your salary is:", "$", sl, sep="")
        break
    else:
        print("invalid number")
        lv = int(input("please get your worker level: "))
