import unittest
import epitran

class TestKabyle(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran("kab-Latn")

    def test_basic_words(self):
        for i, o in [
            ("taqcict", "θɑqʃiʃt"),      # a backs to ɑ near q; final t stays t after ʃ
            ("tamellalt", "θæməlːælt"),  # Perfect
            ("axxam", "ɑχːɑm"),          # a backs to ɑ near χː
            ("nniɣ", "nːiʁ"),            # Lowercase input to match map.csv nn -> nː
            ("abrid", "æβrið"),          # final d after i spirantizes to ð
            ("tewwiḍ", "θəwːiðˤ"),       # final ḍ after i spirantizes to ðˤ
        ]:
            tr = self.epi.transliterate(i)
            self.assertEqual(tr, o)
