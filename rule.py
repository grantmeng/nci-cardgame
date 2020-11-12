from config import COLORS

### Define different rules
class SimpleRule:
    def getScore(self, cards):
        score = 0
        for card in cards:
            score += COLORS[card.color] * card.value
        return score

class ComplexRule:
    pass
