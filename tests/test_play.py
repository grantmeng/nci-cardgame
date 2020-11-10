import pytest
from deck import Deck
from player import Player

deck = Deck()
deck.shuffle()
p1 = Player('Player1')
p2 = Player('Player2')
for _ in range(3):
    p1.draw(deck)
    p2.draw(deck)

@pytest.fixture
def deck():
    deck = Deck()
    deck.shuffle()
    return deck

@pytest.fixture
def p1():
    return Player('Player1')

@pytest.fixture
def p2():
    return Player('Player2')

def test_checkWinner(p1, p2):
    if p1.getScore() > p2.getScore():
        assert 'The winner is: Player1'
    elif p1.getScore() < p2.getScore():
        assert 'The winner is: Player2'
    else:
        assert 'Both players win!'
