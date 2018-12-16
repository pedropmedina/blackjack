# Card is going to a the superclass for the type of cards.
# Card is never gonna be instantiated directly.
# Card is going to keep the state inventory for each card
class Card:
    insure = False

    def __init__(self, rank, suit, hard, soft):
        self.rank = rank
        self.suit = suit
        self.hard = hard
        self.soft = soft

    # human representation of the object
    def __str__(self):
        return f'{self.rank} {self.suit}'

    # More techincal representation consisting of Python expression
    # to rebuild the object when passed to eval()
    def __repr__(self):
        return f'{self.__class__.__name__}({self.rank}, {self.suit})'
