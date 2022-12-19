print("Python party tax program - where tax is a party")
income = float(input("get your income: $"))
if income < 100:
    print("you don't pay any tax")
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
