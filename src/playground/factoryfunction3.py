from functools import partial

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

# This method provides a functionality similar to that one
# achive with the factory class, but the implementation is
# bit cleaner
# Notice that since we are using mapping for conditional logic
# there's no need to combine if/elif/else statements
def factoryfunction(rank, suit):
    partial_class = {
        1: partial(AceCard, rank),
        11: partial(FaceCard, rank),
        12: partial(FaceCard, rank),
        13: partial(FaceCard, rank),
    }.get(rank, partial(NumberCard, rank))
    return partial_class(suit)


deck = [
    factoryfunction(rank, suit)
    for rank in range(1, 14)
    for suit in (club, diamond, heart, spade)
]

# Specify what to export from this module when we import * from another module
__all__ = ['factoryfunction']

if __name__ == '__main__':
    print(deck)
