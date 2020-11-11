from card import Card

### Define different rules
class SimpleRule:
    def getScore(self, cards):
        score = 0
        for card in cards:
            score += Card.COLORS[card.color] * card.value
        return score

class ComplexRule:
    pass
