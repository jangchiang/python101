import random
rnum = []
num = int(input("How many random numbers: "))
max_num = int(input("Maximum number: "))
for i in range(num):
    nums = random.randint(0, max_num)
    rnum.append(nums)
max_rnum = max(rnum)
min_rmun = min(rnum)
cnum = random.randint(min_rmun, max_rnum)
print(f"The number are: {rnum}")
print(f"The minimum is: {min_rmun}")
print(f"The maximum is: {max_rnum}")
print(f"A randomly chosen number is: {cnum}")
rnum.reverse()
print(f"The numbers reversed are: {rnum}")
rnum.sort()
print(f"The numbers sorted are {rnum}")