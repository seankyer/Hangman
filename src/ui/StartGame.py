from src.model.GameInstance import GameInstance
from src.model.HangmanWord import HangmanWord


def start_game():
    print("Welcome to Hangman, created by Sean Kyer")
    print("github.com/SeanKyer")
    print("")
    initialize_game()


def initialize_game():
    state_two = True

    while state_two:

        state = True

        print("Please enter the word for your partner to guess!")
        chosen_word = input("Word: ")
        user_word = HangmanWord(chosen_word)
        game = GameInstance(user_word)

        count = 0
        for count in range(0, 50):
            print(" ")
            count = count + 1

        print(game.letters_shown)
        while state:
            guess = input("Input Guess! ")
            game.guess(guess)
            if game.check_game_over():
                print("The word was:")
                print(game.hangman_word.word)
                print("Thanks for playing!")
                state = False

            if game.check_victory():
                print("You Win!")
                state = False

        choice = input("Would you like to play again? y/n")
        if choice == "y":
            count2 = 0
            for count2 in range(0, 50):
                print(" ")
                count = count + 1
        else:
            state_two = False
