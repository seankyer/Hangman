import unittest

from src.model.GameInstance import GameInstance
from src.model.HangmanWord import HangmanWord


class MyTestCase(unittest.TestCase):
    def test_initialize_letters(self):
        test_word = HangmanWord("word")
        test_instance = GameInstance(test_word)
        self.assertEqual(len(test_instance.letters_shown), 4)
        print(test_instance.letters_shown)
        test_word = HangmanWord("Bangaroo")
        test_instance = GameInstance(test_word)
        self.assertEqual(len(test_instance.letters_shown), 8)
        print(test_instance.letters_shown)
