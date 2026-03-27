import random

while True:
    D1 = random.randint(1, 6)
    D2 = random.randint(1, 6)
    D3 = random.randint(1, 6)
    D4 = random.randint(1, 6)
    D5 = random.randint(1, 6)
    total = (D1 + D2 + D3 + D4 + D5)
    print(f"\nDice Rolls: {D1, D2, D3, D4, D5}")
    print(f"Total is: {total}")

    choice = input("Type n for next number or q to quit: ").lower()

    if choice == "q":
        print("Goodby!")
        break