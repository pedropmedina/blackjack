from .card import Card


class AceCard(Card):
    def __init__(self, rank, suit):
        super().__init__('A', suit, 1, 11)
