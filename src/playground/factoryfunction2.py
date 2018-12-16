from ..cards.acecard import AceCard
from ..cards.facecard import FaceCard
from ..cards.numbercard import NumberCard
from ..suit.suit import Suit

# Instantiate Suit for club, diamond, heart, spade
club, diamond, heart, spade = (
    Suit('Club', '♣︎'),
    Suit('Diamond', '♦︎'),
    Suit('Heart', '♥︎'),
    Suit('Spade', '♠︎'),
)

# This implementation separates conditional logic from mapping logic
# since mapping logic corresponding to FaceCard is already
# implemented in the initialization of that class
def factorycard(rank, suit):
    if 1 == rank:
        return AceCard(rank, suit)
    elif 2 <= rank <= 10:
        return NumberCard(rank, suit)
    elif 11 <= rank <= 13:
        return FaceCard(rank, suit)
    else:
        raise NotImplementedError('Rank is out of range')


deck = [
    factorycard(rank, suit)
    for rank in range(1, 14)
    for suit in (club, diamond, heart, spade)
]

print(deck)
