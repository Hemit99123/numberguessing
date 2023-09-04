import random

def play_game(level, max_num, max_hints):
    print(f"\nWelcome to level {level} of this number guessing game!")
    print(f"\nFor this next part, you will be asked to enter a number between 0 and {max_num} to try to guess a randomly generated number.")
    print("\nCREDITS: HEMIT AND JASKEERAT")
    print(f"\nYou've only got {max_hints} hints\n")

    number = random.randint(1, max_num)
    count = 0

    while count < max_hints:
        count += 1
        guess = int(input(f'\nPlease enter a number between 0 and {max_num}:'))

        if number == guess:
            print(f"\nCongratulations! You did it in {count} try/tries.")
            return True
        elif number > guess:
            print("\nYou guessed too small!")
        elif number < guess:
            print("\nYou guessed too high!")

    print(f"\nBetter luck next time! The number was {number}")
    return False

if __name__ == "__main__":
    levels = [
        {"max_num": 20, "max_hints": 3},
        {"max_num": 30, "max_hints": 3},
        {"max_num": 40, "max_hints": 2}
    ]

    for i, level in enumerate(levels, start=1):
        if play_game(i, level["max_num"], level["max_hints"]):
            if i < len(levels):
                print("\nMoving on to the next level...\n")
            else:
                print("\nCongratulations! You finished all levels!")
        else:
            print("\nGame Over! You couldn't complete all levels.")
            break
