"""Adapter: StripDiacritics for spa-Latn for Regrets."""
from epitran.stripdiacritics import StripDiacritics

_sd = StripDiacritics('spa-Latn')

def process(word):
    """Strip specified diacritics from text."""
    return _sd.process(word)
