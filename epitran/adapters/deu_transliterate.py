"""Adapter: German (deu-Latn) transliteration for Regrets."""
from epitran.simple import SimpleEpitran

_epi = SimpleEpitran('deu-Latn', preproc=True, postproc=True, ligatures=False)

def transliterate(text, normpunc=False, ligatures=False):
    """Transliterate German text to IPA."""
    return _epi.transliterate(text, normpunc, ligatures)

def general_trans(text, filter_func, normpunc=False, ligatures=False):
    """General transliteration with filter function."""
    return _epi.general_trans(text, filter_func, normpunc, ligatures)
