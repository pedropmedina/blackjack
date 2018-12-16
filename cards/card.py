# Card is going to a the superclass for the type of cards.
# Card is never gonna be instantiated directly.
# Card is going to keep the state inventory for each card
class Card:
    def __init__(self, rank, suit, hard, soft):
        self.rank = rank
        self.suit = suit
        self.hard = hard
        self.soft = soft
