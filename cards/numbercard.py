from .card import Card


# NumberCard will initialize Card with any rank ranging from 2 to 10
# Notice that hard and soft are string representations, so we wrap int in str
class NumberCard(Card):
    def __init__(self, rank, suit):
        super().__init__(rank, suit, str(rank), str(rank))
