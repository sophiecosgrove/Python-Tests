import pytest
from Pythontasks import uniquesum

def test_isunique():
    assert uniquesum.is_unique(2,5,4) == 11
    assert uniquesum.is_unique(4,4,5) == 5
    assert uniquesum.is_unique(3,6,3) == 6
    assert uniquesum.is_unique(8,9,9) == 8