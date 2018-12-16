from ..cards.acecard import AceCard
from ..cards.facecard import FaceCard
from ..cards.numbercard import NumberCard


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
