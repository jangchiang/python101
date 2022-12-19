def main():
    while True:
        s = int(input("Enter seconds: "))
        if s < 0:
            print("end of the program")
            break
        else:
            convertSeconds(s)


def convertSeconds(s):
    min = s // 60
    sec = s % 60
    print(f"{s} seconds is {min} m {sec} second")
    return s

main()