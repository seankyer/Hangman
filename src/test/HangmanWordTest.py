import unittest

from src.model.HangmanWord import HangmanWord


class HangmanWordTest(unittest.TestCase):
    def setUp(self):
        self.test_word = HangmanWord("word")

    def test_constructor(self):
        self.assertEqual(self.test_word.word, "word")
        self.assertEqual(self.test_word.length, 4)

    def test_get_word_length(self):
        self.assertEqual(self.test_word.get_word_length(), 4)

    def test_does_word_contain_letter(self):
        self.assertTrue(self.test_word.does_word_contain_letter("w"))
        self.assertFalse(self.test_word.does_word_contain_letter("q"))
        self.assertTrue(self.test_word.does_word_contain_letter("word"))
