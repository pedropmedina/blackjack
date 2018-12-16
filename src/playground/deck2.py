import random

from ..suit.suit import Suit
from .factoryfunction3 import factoryfunction as card

club, diamond, heart, spade = (
    Suit('Club', '♣︎'),
    Suit('Diamond', '♦︎'),
    Suit('Heart', '♥︎'),
    Suit('Spade', '♠︎'),
)

# Extending a collection class such as the list
# for the deck example is a better approach than
# a wrapper since we don't have to re-implement list methods
# that come by default with the list class
class Deck(list):
    def __init__(self):
        super().__init__(
            card(rank, suit)
            for rank in range(1, 14)
            for suit in (club, diamond, heart, spade)
        )
        random.shuffle(self)


d = Deck()
hand = [d.pop(), d.pop()]
