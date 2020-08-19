class GameInstance:
    def __init__(self, hangman_word):
        self.lives = 6
        self.hangman_word = hangman_word
        self.guessed_wrong = []
        self.guessed_right = []
        self.letters_shown = ["_"] * hangman_word.get_word_length()

    def guess(self, letter):
        # Checks if player has already guessed that letter
        if len(letter) > 1:
            print("Please only single letter guesses")
        elif self.guessed_wrong.__contains__(letter) or self.guessed_right.__contains__(letter):
            print("You already guessed that!")
        # Checks if player got a correct letter
        elif self.hangman_word.does_word_contain_letter(letter):
            self.update_letters_shown(letter, self.hangman_word.word)
            self.update_guessed_right(letter)
            self.print_letters_shown()
        else:
            self.update_guessed_wrong(letter)
            self.lives = self.lives - 1
            print("That was not correct. You have " + str(self.lives) + " lives remaining")

    def update_letters_shown(self, letter, word):
        length = len(word)
        indexes = []
        x = self.hangman_word.word.find(letter)
        indexes.append(x)
        for i in range(0, length):
            i = self.hangman_word.word.find(letter, i + 1)
            if not i == -1:
                indexes.append(i)
        for i in indexes:
            self.letters_shown[i] = letter

    def update_guessed_right(self, letter):
        self.guessed_right.append(letter)

    def update_guessed_wrong(self, letter):
        self.guessed_wrong.append(letter)

    def print_letters_shown(self):
        print(self.letters_shown)

    def check_game_over(self):
        if self.lives <= 0:
            print("Game Over!")
            return True

    def check_victory(self):
        if not self.letters_shown.__contains__("_"):
            return True
