import random
import collections
import json
from card import Card

### Deck class
class Deck:
    # card's value range, here assume from 0 to 9
    MAX_VALUE = 9

    def __init__(self):
        self.cards, self.done = [], []
        for color in Card.COLORS:
            for value in range(Deck.MAX_VALUE+1):
                self.cards.append(Card(value, color))

    def shuffle(self):
        self.cards += self.done
        self.done = []
        for i in range(len(self.cards)):
            r = random.randint(0, len(Card.COLORS) * (Deck.MAX_VALUE+1) - 1)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw(self):
        if self.isEmpty(): raise Exception('No card in deck')
        card = self.cards.pop()
        self.done.append(card)
        return card

    def sortCards(self, cards, colors):
        data = collections.defaultdict(list)
        for card in cards:
            data[card.color].append(card.value)
        res = []
        for color in colors:
            if color in data:
                data[color].sort()
                res += [(color, value) for value in data[color]]
        return res

    def isEmpty(self):
        return self.cards == []

    def __str__(self):
        cards = collections.defaultdict(list)
        for card in self.cards:
            cards[card.color].append(card.value)
        return json.dumps(cards)

if __name__ == "__main__":
    deck = Deck()
    print('Got new deck')
    print(deck)
    deck.shuffle()
    print('Deck shuffled')
    print(deck)
    card = deck.draw()
    print('Drawed one card')
    print(card)
    print('Deck after drawing card')
    print(deck)
