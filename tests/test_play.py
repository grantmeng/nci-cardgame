import pytest
from deck import Deck
from player import Player
from play import checkWinner

@pytest.fixture
def deck():
    deck = Deck()
    deck.shuffle()
    return deck

@pytest.fixture
def players():
    return [Player('Player1'), Player('Player2')]

def test_checkWinner(deck, players):
    for _ in range(3):
        for player in players:
            player.draw(deck)

    winner_score = max(player.getScore() for player in players)
    winners = [player.name for player in players if player.getScore() == winner_score]
    assert winners == checkWinner(players)
