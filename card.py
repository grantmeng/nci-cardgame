### Card class
class Card:
    # assume below three colors with corresponding point
    COLORS = {
        'red': 3,
        'yellow': 2,
        'green': 1
    }

    def __init__(self, value, color):
        self.value = value
        self.color = color
        self.points = Card.COLORS[color] * value

    def __str__(self):
        return '{} {}: {}'.format(self.value, self.color, self.points)

if __name__ == "__main__":
    card = Card(2, 'red')
    print(card)
