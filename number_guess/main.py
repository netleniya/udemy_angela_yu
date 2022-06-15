import random

EASY_LEVEL = 10
HARD_LEVEL = 5


def set_difficulty():
    """Set the difficulty level. Return difficulty level as global variable"""
    difficulty = input("Choose a difficulty level: E[asy] or H[ard]: ").lower()

    if difficulty.startswith('h'):
        return HARD_LEVEL
    else:
        return EASY_LEVEL


def main():
    print("Welcome to the Number Guessing Game.")

    n_attempts = set_difficulty()

    my_number = random.randint(1, 100)

    print("I'm thinking of a number between 1 and 100...")

    print(f"You have {n_attempts} attempts remaining to guess the number")

    while n_attempts > 0:
        guess = int(input("Make a guess: "))
        n_attempts -= 1

        if guess > my_number:
            print("Too High")
        elif guess < my_number:
            print("Too low")
        else:
            print(
                f"Well done. You guessed {my_number} with {n_attempts} guesses remaining!")
            break
        print(f"You have {n_attempts} attempts left.")

    else:
        print("Better luck next time.")


if __name__ == "__main__":
    main()
