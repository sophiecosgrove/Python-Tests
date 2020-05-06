import pytest
from Pythontasks import blackjack

def test_blackjack():
    assert blackjack.blackjack(22,22) == 0
    assert blackjack.blackjack(32,8) == 8
    assert blackjack.blackjack(21,65) == 21
    assert blackjack.blackjack(13,18) == 18
    assert blackjack.blackjack(19,4) == 19
    assert blackjack.blackjack(21,21) == 0
    assert blackjack.blackjack(45,67) == 0
    assert blackjack.blackjack(7,0) == 7