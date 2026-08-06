import unittest
import epitran

class TestKabyle(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran("kab-Latn")

    def test_basic_words(self):
        for i, o in [
            ("taqcict", "θɑqʃiʃt"),      # a backs to ɑ near q; final t stays t after ʃ
            ("tamellalt", "θæməlːælt"),  # lt blocks spirantization
            ("axxam", "ɑχːɑm"),          # a backs to ɑ near χː
            ("nniɣ", "nːiʁ"),            # nn stays long stop
            ("abrid", "æβrið"),          # final d after i spirantizes to ð
            ("tewwiḍ", "θəwːiðˤ"),       # final ḍ after i spirantizes to ðˤ
            ("argaz", "ærɡæz"),          # g is blocked after r
            ("weltma", "wəltmæ"),        # t is blocked after l
        ]:
            tr = self.epi.transliterate(i)
            self.assertEqual(tr, o)
