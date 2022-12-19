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
