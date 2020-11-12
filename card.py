### Card class
class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color

    def __str__(self):
        return '{} {}'.format(self.color, self.value)

if __name__ == "__main__":
    card = Card(2, 'red')
    print(card)
