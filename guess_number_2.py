import random

number = random.randint(1, 100)

guess = int(input("Choose a number 1 to 100: "))

while guess != number:
    diff = abs(guess - number)

    if diff <= 5:
        print("You are close!")
    elif guess > number:
        print("Your guess is too high")
    else:
        print("Your guess is too low")

    guess = int(input("Try again: "))

print("You guessed it!")