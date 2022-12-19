"""2. Parity"""

#part1
def displayParity(num):
    parity = num % 2
    print(parity)


#part2
def getParity(num):
    parity = num % 2
    return parity


#part3
def isOdd(num):
    if getParity(num) == 1:
        return True
    else:
        return False



