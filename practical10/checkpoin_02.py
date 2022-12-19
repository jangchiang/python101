"""Check point 02 List"""
# q3.Number List
numlist = []
minum = int(input("Enter your minimum number: "))
maxnum = int(input("Enter your maximum number: "))
while minum > maxnum:
    print(f'Your maximum must be greater than {minum}')
    maximum = int(input("Enter your maximum number: "))
for i in range(minum, maxnum + 1):
    numlist.append(i)
print(numlist)
'''End of q3'''


# q4.Subject List
def main():
    codelist = []
    subject_input(codelist)
    codelist.sort()
    print(f"you want to do these {len(codelist)} subjects: ")
    for i in codelist:
        print(i)
    for subject in codelist:
        if subject == "CP1401":
            print(f"you have CP1401, you are cool")
    print("End of the program")


def subject_input(codelist):
    while True:
        subject = str(input("Enter your subject code: ")).upper()
        if subject == "":
            break
        elif subject_condition(subject):
            codelist.append(subject)
        else:
            print("invalid subject code.")


def subject_condition(code):
    s = code[0:2]
    s.isupper()
    digit = code[2:]
    digit.isdigit()
    if len(code) != 6:
        return False
    elif len(s) != 2:
        return False
    elif len(digit) != 4:
        return False
    elif digit.isdigit():
        return True
    else:
        return False


main()

'''end of q4'''
