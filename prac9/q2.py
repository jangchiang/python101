def getTime(timeList):
    while True:
        time = int(input("Enter the time(0-23): "))
        if time > 23:
            break
        elif time < 0:
            break
        else:
            timeList.append(time)


def main():
    timelist = []
    afternoon = []
    getTime(timelist)
    print(f"time which you order: {timelist}")
    for time in timelist:
        if time > 12:
            afternoon.append(time)
    print(f"in order have {afternoon}. it is afternoon")


main()