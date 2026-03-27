import random

number = random.randint(1, 100)

while True:
    try:
        guess = int(input("Choose a number 1 to 100: "))
        break
    except:
        print("Invalid entry, please enter a whole number.")

while guess != number:
   # if guess - number <= 5: 
    #    print("Too high, but you are close")
    #elif number - number <= 5: 
     #   print("Too low, but you are close")
    if guess > number:
        print("Your guess is too high")
    else:
        print("Your guess is too low")

    while True:
        try:
            guess = int(input("Try again: "))
            break
        except:
            print("Invalid entry, please enter a whole number.")

print("You guessed it!")

#  if int(guess - number >= 5): print("Too high, but you are close")
 #   elif number-guess >= 5: print("Too low, but you are close")