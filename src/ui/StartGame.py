from src.model.GameInstance import GameInstance
from src.model.HangmanWord import HangmanWord


def start_game():
    print("Welcome to Hangman, created by Sean Kyer")
    print("github.com/SeanKyer")
    print("")

    state = True

    print("Please enter the word for your partner to guess!")
    chosen_word = input("Word: ")
    user_word = HangmanWord(chosen_word)
    game = GameInstance(user_word)

    count = 0
    for count in range(0, 50):
        print(" ")
        count = count + 1

    while state:
        guess = input("Input Guess! ")
        game.guess(guess)
        if game.check_game_over():
            print("Thanks for playing!")
            state = False
        if game.check_victory():
            print("You Win!")
            state = False

