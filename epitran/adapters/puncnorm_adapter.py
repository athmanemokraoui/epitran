"""Adapter: PuncNorm for Regrets."""
from epitran.puncnorm import PuncNorm

_pn = PuncNorm()

def norm(text):
    """Normalize punctuation in text."""
    return _pn.norm(text)
