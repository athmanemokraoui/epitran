"""Adapter: Spanish word_to_tuples for Regrets."""
from epitran.simple import SimpleEpitran

_epi = SimpleEpitran('spa-Latn', preproc=True, postproc=True, ligatures=False)

def word_to_tuples(text, normpunc=False):
    """Word to tuples — detailed segment analysis."""
    return _epi.word_to_tuples(text, normpunc)
