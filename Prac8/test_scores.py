"""
pseudocode
get grade function:
    85 <= score <= 100 = HD
    75 <= score <= 84 = D
    65 <= score <= 74 = C
    50 <= score <= 64 = C
    score < 50 = N

display grade:
    for i in range(len(score)):
    grade = get_grade(score[i])
    print(f'Score {i} is {score[i]}, which is {grade}')

main function:
    get score function:
    display grade function:
    display average
"""
def get_grade(score):
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


def display(score):
    for i in range(len(score)):
        grade = get_grade(score[i])
        print(f'Score {i+1} is {score[i]}, which is {grade}')


def main():
    listscore = []
    for i in range(1, 4 + 1):
        mark = float(input(f'Score {i}: '))
        listscore.append(mark)
    display(listscore)
    average = sum(listscore) / len(listscore)
    print(f'The average score was {average}')


main()