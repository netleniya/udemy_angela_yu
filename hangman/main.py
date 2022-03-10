import os
import random
from hangman_art import logo, stages
from hangman_words import word_list


def play():
    ''' '''
    candidate = random.choice(word_list)
    word_length = len(candidate)
    display = list()

    for _ in range(word_length):
        display += '_'

    lives = len(stages) - 1
    end_game = False

    while not end_game:

        guess = input("Guess a letter: ").lower()

        os.system('clear')

        for pos in range(word_length):
            letter = candidate[pos]
            if letter == guess:
                display[pos] = letter

        print(f"{' '.join(display)}")

        if guess not in candidate:
            lives -= 1
            print(stages[lives])

            if lives < 1:
                end_game = True
                print("You lose.")
                print(f"Correct answer was: {candidate}")

        if '_' not in display:
            end_game = True
            print("You Win!")


def main():

    print(logo)

    greeting = '''
    Welcome to Hangman. Guess correctly to stay alive. If you lose you get the noose!
    '''
    print(greeting)

    play_on = True

    while play_on:

        answer = input("Play? (Y/N): ").lower()
        if answer == 'y':
            play()
        else:
            print("Okay, Bye...")
            play_on = False


if __name__ == "__main__":
    main()
