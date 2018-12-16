from .card import Card


# FaceCard is gonna handle the initialization for cards within the range
# 11 and 13.
# Since 11, 12, 13 are equivalent to letters, we have a dictionary to
# map each number to the corresponding letter "rank"
class FaceCard(Card):
    def __init__(self, rank, suit):
        card_rank = {11: 'J', 12: 'Q', 13: 'K'}.get(rank)
        super().__init__(card_rank, suit, 10, 10)
