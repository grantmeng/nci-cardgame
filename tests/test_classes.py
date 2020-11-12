from config import MAX_CARD_VALUE, COLORS
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
    for color in COLORS:
        assert sorted(colors[color]) == list(range(MAX_CARD_VALUE+1))

def test_player():
    p = Player('NCI')
    assert p.name == 'NCI'
    assert isinstance(p.rule, SimpleRule)
    assert not p.hand

def test_rule():
    cards = [Card(2, 'red'), Card(1, 'green')]
    r = SimpleRule()
    assert  2 * COLORS['red'] + 1 * COLORS['green'] == r.getScore(cards)
