import random

from ..suit.suit import Suit
from .factoryfunction3 import factoryfunction as cards

club, diamond, heart, spade = (
    Suit('Club', '♣︎'),
    Suit('Diamond', '♦︎'),
    Suit('Heart', '♥︎'),
    Suit('Spade', '♠︎'),
)

# Casinos deal half a dozen decks of cards from a shoe
# all mingled together. For this reason, extending a class
# collection is not possible. From the tree composite objects
# options (wrap, extend and invent), inventing a new class
# is necessary in order to add the features required by the casino
# to add more than one deck
# Another rule of casinos is that no all cards are dealt in the shoe,
# a marker card is inserted and given the rank in that marker card
# cards will be removed from the shoe

# This new class is going to extend the list class collection
# and add new functionality to it. The way the list is initialize
# must vary from the extended version in deck2 as now
# we also must take into consideration the iterations for the number
# of decks used in the game (half a dozen)
class Deck(list):
    def __init__(self, decks=1):
        super().__init__()
        for _ in range(decks):  # number of decks needed
            self.extend(
                cards(rank, suit)
                for rank in range(1, 14)
                for suit in (club, diamond, heart, spade)
            )
        random.shuffle(self)
        burn = random.randint(1, 52)
        for _ in range(burn):
            self.pop()
