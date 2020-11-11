import json
from player import Player
from deck import Deck

def checkWinner(p1, p2):
    for player in (p1, p2):
        print('Name: {}, Score: {}, Cards: {}'.format(player.name, player.getScore(), player.showHandByColor()))
    if p1.getScore() > p2.getScore():
        print('The winner is: {}'.format(p1.name))
    elif p1.getScore() < p2.getScore():
        print('The winner is: {}'.format(p2.name))
    else:
        print('Both players win!')

### create a new deck and shuffle it
deck = Deck()
deck.shuffle()

### create card list and test the sort function per required
cards = []
for _ in range(5):
    cards.append(deck.draw())
colors = ['yellow', 'green', 'red']
sortedCards = deck.sortCards(cards, colors)
print('Sorted cards: {}'.format(sortedCards))

### create two players
p1 = Player('Player1')
p2 = Player('Player2')

### each player draws 3 cards by turn
for _ in range(3):
    p1.draw(deck)
    p2.draw(deck)

### check the winner
checkWinner(p1, p2)


