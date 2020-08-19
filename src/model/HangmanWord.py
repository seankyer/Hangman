from re import search


class HangmanWord:
    def __init__(self, word):
        self.word = word
        self.length = len(word)

    # returns int of length of self word
    def get_word_length(self):
        return len(self.word)

    # Return true or false depending on if letter is found in word
    def does_word_contain_letter(self, letter):
        if search(letter, self.word):
            return True
        else:
            return False
