class SimpleRule:
    def getScore(self, cards):
        score = 0
        for card in cards:
            score += card.points
        return score
