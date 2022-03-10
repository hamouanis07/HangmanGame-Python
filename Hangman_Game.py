import os
import random
import sys

#   Make a list of words
words = [
    "apple",
    "banana",
    "orange",
    "coconut",
    "strawberry",
    "lime",
    "grapefruit",
    "lemon",
    "kumquat",
    "blueberry",
    "melon"
]


def clear():
    if os.name == 'nt':     # all modern windows
        os.system('cls')
    else:                   # if on mac
        os.system('clear')


def clear2():
    print("\n" * 10)


def draw(bad_guesses, good_guesses, secret_word):
    #   Draw spaces
    #   Draw guessed letters and strikes

    clear2()

    print('Strikes: {}/7\n'.format(len(bad_guesses)))

    print("Missed letters:    ", end='')
    for letter in bad_guesses:
        print(letter, end=' ')
    print("\n\n")

    for letter in secret_word:
        if letter in good_guesses:
            print(letter, end='')  # end=''    is to print on the same line

        else:
            print('_', end='')

    print('')


def get_guess(bad_guesses, good_guesses):
    while True:
        #   Take guess
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("You can only guess a single letter!")

        elif guess in good_guesses or guess in bad_guesses:
            print("You've already guessed that letter!")

        elif not guess.isalpha():  # checks if all characters in guess are letters
                print("You can only guess letters")

        else:
            return guess


def play(done):
    clear2()

    #   Pick a random word
    secret_word = random.choice(words)
    bad_guesses = []
    good_guesses = []

    #   print out win/lose
    while True:
        draw(bad_guesses, good_guesses, secret_word)
        guess = get_guess(bad_guesses, good_guesses)

        if guess in secret_word:
            good_guesses.append(guess)

            found = True

            for letter in secret_word:
                if letter not in good_guesses:
                    found = False

            if found:
                print('You win!')
                print('The secret word was {}'.format(secret_word))
                done = True

        else:
            bad_guesses.append(guess)
            if len(bad_guesses) == 7:
                draw(bad_guesses, good_guesses, secret_word)
                print('You lost!')
                print('The secret word word {}'.format(secret_word))
                done = True

        if done:
            play_again = input("Play again? Y/N").lower()
            if play_again == 'y':
                return play(done=False)
            else:
                sys.exit()


def welcome():
    start = input("Press enter/return to start, or Q to quit").lower()
    if start == 'Q':
        print("Bye!")
        sys.exit()
    else:
        return True


print("Welcome to Hangman Game!")

done = False

while True:
    clear2()

    welcome()
    play(done=done)
