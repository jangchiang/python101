"""3. JCU Grades"""

import random

def standard_of_grade(score):
    if 85 <= score <= 100:
        grade = "HD"
    elif 75 <= score <= 84:
        grade = "D"
    elif 65 <= score <= 74:
        grade = "C"
    elif 50 <= score <= 64:
        grade = "P"
    elif score < 50:
        grade = "N"
    else:
        grade = "it has some thing wrong"
    return grade

def print_grade():
    while True:
        mark = float(input("get your score: "))
        if 0 <= mark <= 100:
            grade = (standard_of_grade(mark))
            print(grade)
        else:
            break

def main():
    print_grade()
    round_time = int(input("How many random scores: "))
    for time in range(round_time):
        random_score = random.randint(0, 100)
        grade = standard_of_grade(random_score)
        print(f"{random_score} = {grade}\n")
main()
