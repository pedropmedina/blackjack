from ..cards.acecard import AceCard
from ..cards.facecard import FaceCard
from ..cards.numbercard import NumberCard
from ..suit.suit import Suit

# Instantiate Suit
club, diamond, heart, spade = (
    Suit('Club', '♣︎'),
    Suit('Diamond', '♦︎'),
    Suit('Heart', '♥︎'),
    Suit('Spade', '♠︎'),
)

# Here class_, rank_str are dynamically set in the
# object once we run rank.
# Notice that rank returns self as this needed in order
# to then, chain suit to it
class FactoryCard:
    def rank(self, rank):
        self.class_, self.rank_str = {
            1: (AceCard, rank),
            11: (FaceCard, rank),
            12: (FaceCard, rank),
            13: (FaceCard, rank),
        }.get(rank, (NumberCard, rank))
        return self

    def suit(self, suit):
        return self.class_(self.rank_str, suit)


deck = [
    FactoryCard().rank(rank).suit(suit)
    for rank in range(1, 14)
    for suit in (club, diamond, heart, spade)
]

print(deck)
