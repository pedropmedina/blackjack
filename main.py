from cards.acecard import AceCard
from cards.facecard import FaceCard
from cards.numbercard import NumberCard
from suit.suit import Suit

# There are four Suits to be initialized:
# Club, Diamond, Heart, Spade
# Use unpacking to assign initialized Suit to each variable,
#  we could have also initialize one at a time
club, diamond, heart, spade = (
    Suit('Club', '♣︎'),
    Suit('Diamond', '♦︎'),
    Suit('Heart', '♥︎'),
    Suit('Spade', '♠︎'),
)

# factory function
def card(rank, suit):
    if 1 == rank:
        return AceCard(rank, suit)
    elif 2 <= rank <= 10:
        return NumberCard(rank, suit)
    elif 11 <= rank <= 13:
        return FaceCard(rank, suit)
    else:
        raise NotImplementedError('Rank is out of range')


# This is another approach to acomplish the above. We use a
# Class Factory instead and organize the logic inside
class CardFactory:
    def rank(self, rank):
        self.class_, self.rank_str = {
            1: (AceCard, 'A'),
            11: (FaceCard, 'J'),
            12: (FaceCard, 'Q'),
            13: (FaceCard, 'K'),
        }.get(rank, (NumberCard, rank))
        return self

    def suit(self, suit):
        return self.class_(self.rank_str, suit)


deck = [
    card(rank, suit)
    for rank in range(1, 14)
    for suit in (club, diamond, heart, spade)
]

print(deck)
