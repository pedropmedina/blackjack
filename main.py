import random

from cards.acecard import AceCard
from cards.facecard import FaceCard
from cards.numbercard import NumberCard
from suit.suit import Suit

# Suit initializes four constant objects:
# Club, Diamond, Heart, Spade

# They're constant objects, because, we won't be instantiating, mutating them
# on every use, instead, they'll always be the same as they get
# passed as argument to suit parameter in Card

# Use unpacking to assign initialized Suit to each variable,
#  we could have also initialize one at a time
club, diamond, heart, spade = (
    Suit('Club', '♣︎'),
    Suit('Diamond', '♦︎'),
    Suit('Heart', '♥︎'),
    Suit('Spade', '♠︎'),
)

# This is known as a Fluent interface for object construction
class CardFactory:
    def rank(self, rank):
        self.class_, self.rank_str = {
            1: (AceCard, 'A'),
            11: (FaceCard, 'J'),
            12: (FaceCard, 'Q'),
            13: (FaceCard, 'K'),
        }.get(rank, (NumberCard, str(rank)))
        return self

    def suit(self, suit):
        return self.class_(self.rank_str, suit)


deck = [
    CardFactory().rank(rank).suit(suit)
    for rank in range(1, 14)
    for suit in (club, diamond, heart, spade)
]

random.shuffle(deck)

hand = [deck.pop(), deck.pop()]

print(hand)
