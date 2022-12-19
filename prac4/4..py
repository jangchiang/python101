#4.1 aveerge age
print("mission A: Average age")
s = -1
ta = 0
n = 0
while True:
    age = int(input("Enter age: "))
    if age == s:
        break
    ta += age
    n+=1
    aa = ta/n
    print("average is: ", aa)