#4.3 Total number
tn = 0
nc = int(input("How many times do you want to count: "))
for nc in range(nc):
    n = float(input("get number"+ str(nc+1) + ": "))
    nc +=1
    tn = tn + n
print("total those ", nc, " number is: ", "%.2f"%tn, sep="")
