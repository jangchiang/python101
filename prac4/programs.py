# 1.error Checking
lv = int(input("please get your worker level: "))
while True:
    if lv in range(1, 11):
        sl = lv * 5000
        print("your worker is: ", lv, " your salary is:", "$", sl, sep="")
        break
    else:
        print("invalid number")
        lv = int(input("please get your worker level: "))

# 2.Number Sequences: a, b
print("mission A")
for i in range(1, 100, 2):
    print(i, end=", ")
else:
    print("finish")
print("mission B")
for i in range(1896, 2021, 4):
    print(i, end=' ')
else:
    print("finish")

# 3.menu for smileys
print("Menu")
print("(S)miley")
print("(F)rowny")
print("(Q)uit")
m = input("Enter choice: ")
while True:
    if m == 's':
        print(":)")
        break
    if m == 'f':
        print(":(")
        break
    if m == 'q':
        print("ok quit menu")
        break
    else:
        print("please type in menu choice")
        m = input("Enter choice: ")

# 4.1 aveerge age
print("mission A: Average age")
s = -1
ta = 0
n = 0
while True:
    age = int(input("Enter age: "))
    if age == s:
        break
    ta += age
    n += 1
    aa = ta/n
    print("average is: ", aa)

# 4.2 Smileys count
sc = 0
fc = 0
print("Menu")
print("(S)miley")
print("(F)rowny")
print("(Q)uit")
m = input("Enter choice: ")
while True:
    if m == 's':
        print(":)")
        sc += 1
        m = input("Enter choice: ")
    if m == 'f':
        print(":(")
        fc += 1
        m = input("Enter choice: ")
    if m == 'q':
        print("ok quit menu")
        print("you print smile: ", sc, " times and frown: ", fc, "times", sep="")
        break
    else:
        print("please type in menu choice")
        m = input("Enter choice: ")

# 4.3 Total number
tn = 0
nc = int(input("How many times do you want to count: "))
for nc in range(nc):
    n = float(input("get number" + str(nc+1) + ": "))
    nc += 1
    tn = tn + n
print("total those ", nc, " number is: ", "%.2f" % tn, sep="")

# 5.Guessing Game
SECRET = 6
guess = int(input("Guess a number: "))
while guess != SECRET:
    if guess >= 4 or guess <= 8:
        print("Closer")
        guess = int(input("Guess a number: "))
    if guess < 4:
        print("higher", guess)
        guess = int(input("Guess a number: "))
    if guess > 8:
        print("lower", guess)
        guess = int(input("Guess a number: "))
print("You got it!")