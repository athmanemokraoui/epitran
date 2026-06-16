"""Adapter: Spanish strict transliteration for Regrets."""
from epitran.simple import SimpleEpitran

_epi = SimpleEpitran('spa-Latn', preproc=True, postproc=True, ligatures=False)

def strict_trans(text, normpunc=False, ligatures=False):
    """Strict transliteration — unmapped characters omitted."""
    return _epi.strict_trans(text, normpunc, ligatures)

def general_trans(text, filter_func, normpunc=False, ligatures=False):
    """General transliteration with filter function."""
    return _epi.general_trans(text, filter_func, normpunc, ligatures)
