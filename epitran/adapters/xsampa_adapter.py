"""Adapter: XSampa for Regrets."""
from epitran.xsampa import XSampa

_xs = XSampa()

def ipa2xs(ipa):
    """Convert IPA string to X-SAMPA."""
    return _xs.ipa2xs(ipa)

def longest_prefix(s):
    """Find longest matching prefix in trie."""
    return _xs.longest_prefix(s)
