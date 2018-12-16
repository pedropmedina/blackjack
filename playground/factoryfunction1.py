from ..cards.acecard import AceCard
from ..cards.facecard import FaceCard
from ..cards.numbercard import NumberCard
from ..suit.suit import Suit

# Instantiate suit for Club, Diamond, Heart, Spade
Club, Diamond, Heart, Spade = (
    Suit('Club', '♣︎'),
    Suit('Diamond', '♦︎'),
    Suit('Heart', '♥︎'),
    Suit('Spade', '♠︎'),
)

# The first implentation of factory function is more verbose
# as it contains conditional and mapping all together which is not
# best practice
# THIS EXAMPLE WON'T WORK AS I HAVE ALREADY DESIGNED FaceCard TO
# IMPLEMENT MAPPING LOGIC AT INITIALIZATION
def factory_card(rank, suit):
    if 1 == rank:
        return AceCard(rank, suit)
    elif 2 <= rank <= 10:
        return NumberCard(rank, suit)
    elif rank <= 11 <= 13:
        mapped_rank = {11: 'J', 12: 'Q', 13: 'K'}.get(rank)
        return FaceCard(mapped_rank, suit)
    else:
        raise NotImplementedError('Rank is out of range')
