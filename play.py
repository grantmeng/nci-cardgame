import json
from config import NUM_OF_PLAYER, NUM_OF_CARD
from player import Player
from deck import Deck

def checkWinner(players):
    winner_score = max(player.getScore() for player in players)
    winners = [player.name for player in players if player.getScore() == winner_score]
    return winners

### create a new deck and shuffle it
deck = Deck()
deck.shuffle()

### create card list and test the sort function per required
cards = []
for _ in range(5):
    cards.append(deck.draw())
print('Draw 5 cards: {}'.format(','.join('({} {})'.format(card.color, card.value) for card in cards)))
colors = ['yellow', 'green', 'red']
print('Color order: {}'.format(colors))
sortedCards = deck.sortCards(cards, colors)
print('Sorted cards: {}'.format(sortedCards))
print()

### create players
players = []
for i in range(NUM_OF_PLAYER):
    player = Player('Player' + str(i))
    players.append(player)

### each player draws card by turn
for _ in range(NUM_OF_CARD):
    for player in players:
        player.draw(deck)

print('After players drawing card:')
for player in players:
    print(player)

### check the winner
winners = checkWinner(players)
print('Winners: {}'.format(winners))
