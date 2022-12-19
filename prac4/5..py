#5.Gussing Game
SECRET = 6
guess = int(input("Guess a number: "))
while guess != SECRET:
    if guess >= 4 or guess<= 8:
        print("Closeer")
        guess = int(input("Guess a number: "))
    if guess < 4:
        print("higher", guess)
        guess = int(input("Guess a number: "))
    if guess > 8:
        print("lower", guess)
        guess = int(input("Guess a number: "))
print("You got it!")