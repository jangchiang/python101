def get_valid_number(prompt):
    while True:
        number = int(input(prompt))
        if number > 0:
            return number
        else:
            print("Invalid number!")


def convert_m_to_km(speed_in_m):
    km = speed_in_m * 0.621371
    return km


def determine_fine(km_speed, limit_speed):
    determine = km_speed - limit_speed
    if 0 < determine <= 13:
        fine = 177
        dp = 1
        print(f"your speed is: {km_speed:.2f} km/h \nyour demerit is {dp}")
    elif 13 < determine <= 20:
        fine = 266
        dp = 3
        print(f"your speed is: {km_speed:.2f} km/h \nyour demerit is {dp}")
    elif 20 < determine <= 30:
        fine = 444
        dp = 4
        print(f"your speed is: {km_speed:.2f} km/h \nyour demerit is {dp}")
    elif 30 < determine <= 40:
        fine = 622
        dp = 6
        print(f"your speed is: {km_speed:.2f} km/h \nyour demerit is {dp}")
    elif determine > 40:
        fine = 1245
        dp = 8
        print(f"your speed is: {km_speed:.2f} km/h \nyour demerit is {dp}")
    else:
        print("you don't have any fines")
    return fine


def main():
    speed_in_m = float(input("get speed in m: "))
    km_speed = convert_m_to_km(speed_in_m)
    limit_speed = get_valid_number("get speed limit in km: ")
    fine = determine_fine(km_speed, limit_speed)
    print(f"fine is ${fine:.2f}")


main()
