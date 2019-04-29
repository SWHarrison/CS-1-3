from redact_words import redact_words
import unittest

class RedactTest(unittest.TestCase):

    def test_redact_some_banned(self):

        words = ['I', 'like', 'tasty', 'pie', 'and', 'tasty', 'beer']
        new_text = redact_words(words,['tasty'])
        assert len(new_text) == 5
        assert new_text[0] == 'I'
        assert new_text[1] == 'like'
        assert new_text[2] == 'pie'
        assert new_text[3] == 'and'
        assert new_text[4] == 'beer'

    def test_redact_no_banned(self):

        new_text = redact_words(['I', 'like', 'tasty', 'pie'],['awful'])
        assert len(new_text) == 4
        assert new_text[0] == 'I'
        assert new_text[1] == 'like'
        assert new_text[2] == 'tasty'
        assert new_text[3] == 'pie'

    def test_redact_all_banned(self):

        new_text = redact_words(['I', 'like', 'tasty', 'pie'],['I', 'like', 'tasty', 'pie'])
        assert len(new_text) == 0

    def test_redact_empty_banned_words(self):

        words = ['I', 'like', 'tasty', 'pie']
        new_text = redact_words(words,[])
        assert len(new_text) == 4
        assert new_text[0] == 'I'
        assert new_text[1] == 'like'
        assert new_text[2] == 'tasty'
        assert new_text[3] == 'pie'
        assert new_text == words

    def test_ssome_banned_words(self):
        words = ["are", "these", "words", "going", "to", "go", "through"]
        banned = ["these", "are", "the", "invalid", "words"]

        assert redact_words(words, banned) == ["going", "to", "go", "through"]

    def test_all_band_words(self):
        words = ["bad", "word"]
        banned = ["bad", "word"]

        assert redact_words(words, banned) == []

    def test_no_banned_words(self):
        words = ["hello", "world"]
        banned = ["bad", "word"]

        assert redact_words(words, banned) == words
