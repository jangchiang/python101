def getValidvalu (values):
    for i in range(0, 5):
        while True:
            value = int(input("Enter the value between 0-100: "))
            if 0 <= value <= 100:
                values.append(value)
                break
            else:
                print("Invalid value")


def main():
    vlist = []
    getValidvalu(vlist)
    total = sum(vlist)
    nummax = max(vlist)
    nummin = min(vlist)
    print(vlist, sep="")
    print(f"total: {total}")
    print(f"highest: {nummax}")
    print(f"lowest: {nummin}")


main()