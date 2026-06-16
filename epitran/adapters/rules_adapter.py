"""Adapter: Rules for Regrets — empty rules for basic test."""
from epitran.rules import Rules

_rules = Rules([])

def apply(text):
    """Apply context-sensitive rules to text."""
    return _rules.apply(text)
