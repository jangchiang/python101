hc = float(75)
dfc = float(input("get daily food cost: $"))
dac = float(input("get daily activities cost: $"))
nod = int(input("get the number of day: "))
tc = (hc + dfc + dac)*nod
print("The trip will cost: $", "%.2f"%tc)