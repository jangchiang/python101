#4.2 Smileys count
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
