import random

from ..suit.suit import Suit
from .factoryfunction3 import factoryfunction as card

club, diamond, heart, spade = (
    Suit('Club', '♣︎'),
    Suit('Diamond', '♦︎'),
    Suit('Heart', '♥︎'),
    Suit('Spade', '♠︎'),
)

# Instead of using the built in list class as follow to create a deck,
# we can wrap the behavior inside a class Deck as show below:
# deck = [
#     CardFactory().rank(rank).suit(suit)
#     for rank in range(1, 14)
#     for suit in (club, diamond, heart, spade)
# ]

# random.shuffle(deck)

# hand = [deck.pop(), deck.pop()]

# Composite objects are like containers
# This is an example of wrapped composite object
# This wrapper around a list leads to a bit of repetition
# since we have to define pop in the class when list already implement pop
# by default
class Deck:
    def __init__(self):
        self._cards = [
            card(rank, suit)
            for rank in range(1, 14)
            for suit in (club, diamond, heart, spade)
        ]
        random.shuffle(self._cards)

    def pop(self):
        return self._cards.pop()


d = Deck()
hand = [d.pop(), d.pop()]
