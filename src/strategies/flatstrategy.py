from .bettingstrategy import BettingStrategy


class FlatStrategy(BettingStrategy):
    def bet(self):
        return 1
