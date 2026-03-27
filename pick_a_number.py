import random

while True:
    number = random.randint(1, 10)
    print(f"\nYour number is: {number}")

    choice = input("Type n for next number or q to quit: ").lower()

    if choice == "q":
        print("Goodby!")
        break