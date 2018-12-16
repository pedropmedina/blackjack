import random

from ..factory.cardfactory import CardFactory
from ..suit.suit import Suit

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

# Instantiate Fluent Card Interface
card = CardFactory()


class Deck(list):
    def __init__(self, decks=1):
        super().__init__()
        for _ in range(decks):
            self.extend(
                card.rank(r).suit(s)
                for r in range(1, 14)
                for s in (club, diamond, heart, spade)
            )
        random.shuffle(self)
        marker = random.randint(1, 52)
        for _ in range(marker):
            self.pop()

    def __bool__(self):
        return bool(self)
