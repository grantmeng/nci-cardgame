from card import Card
from deck import Deck
from player import Player
from rule import SimpleRule
import collections

def test_card():
    card = Card(2, 'red')
    assert card.value == 2
    assert card.color == 'red'

def test_deck():
    deck = Deck()
    colors = collections.defaultdict(list)
    for card in deck.cards:
        colors[card.color].append(card.value)
    assert sorted(colors['red']) == list(range(10))
    assert sorted(colors['green']) == list(range(10))
    assert sorted(colors['yellow']) == list(range(10))

def test_player():
    p = Player('NCI')
    assert p.name == 'NCI'
    assert isinstance(p.rule, SimpleRule)
    assert not p.hand
