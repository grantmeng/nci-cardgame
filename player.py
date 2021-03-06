import collections
import json
from deck import Deck
from rule import SimpleRule

### Player class
class Player:
    ### can use diff rules, default is the simple rule defined in Rule class
    def __init__(self, name, rule=SimpleRule):
        self.name = name
        self.rule = rule()
        self.hand = []

    def draw(self, deck):
        card = deck.draw()
        self.hand.append(card)
        return card

    def getHand(self):
        return self.hand

    def showHand(self):
        cards = []
        for card in self.hand:
            cards.append('{} {}'.format(card.color, card.value))
        return ','.join(cards)

    def showHandByColor(self):
        cards = collections.defaultdict(list)
        for card in self.hand:
            cards[card.color].append(card.value)
        return json.dumps(cards)

    def getScore(self):
        return self.rule.getScore(self.hand)

    def __str__(self):
        return '{}: {}, Score: {}'.format(self.name, self.showHandByColor(), self.getScore())

if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()
    p1 = Player('Player1')
    p2 = Player('Player2')
    for _ in range(3):
        p1.draw(deck)
        p2.draw(deck)
    for player in (p1, p2):
        print('Name: {}, Score: {}, Cards: {}'.format(player.name, player.getScore(), player.showHandByColor()))
