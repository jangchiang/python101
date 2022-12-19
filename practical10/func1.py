"""func1"""


# section A
def hyphenf():
    hyphens = 40
    for i in range(hyphens):
        print("-", end="")


# section B
def parity(num):
    parity = num % 2
    return parity


def evencheck(num):
    if parity(num) == 0:
        print("Even")
    else:
        print("odd")


evencheck()
