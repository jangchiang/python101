def calculate_bmi(height, weight):
    bmi = weight / height ** 2
    return bmi


def determine_weight_category(bmi):
    if bmi < 18.5:
        return "underweight"
    elif 18.5 <= bmi >= 25:
        return "normal"
    elif 25 <= bmi > 30:
        return "overweight"
    else:
        return "obese"

def main():
    height = 1.75
    for weight in range(50, 102, 2):
        bmi = calculate_bmi(height, weight)
        Cat = determine_weight_category(bmi)
        print(f"Height {height}m, Weight {weight}kg, BMI{bmi:.1f}, considered {Cat}")
        


main()
