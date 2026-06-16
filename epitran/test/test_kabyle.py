import unittest
import epitran

class TestKabyle(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran("kab-Latn")

    def test_basic_words(self):
        for i, o in [
            ("taqcict", "θæqʃiʃθ"),
            ("tamellalt", "θæməlːælt"),
            ("axxam", "æχːæm"),
            ("Nniɣ", "nːiʁ"),
            ("abrid", "æβrid"),
            ("tewwiḍ", "θəwːidˤ"),
        ]:
            tr = self.epi.transliterate(i)
            self.assertEqual(tr, o)
