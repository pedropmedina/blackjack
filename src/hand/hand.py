# By gathering args in a single statement while initializing the
# Hand, we avoid multiple method calls which add complexity and is more
# error prompt
class Hand:
    def __init__(self, dealer_card, *args):
        self.dealer_card = dealer_card
        self.cards = list(args)

    @staticmethod
    def freeze(other):
        hand = Hand(other.dealer_card, *other.cards)
        return hand

    @staticmethod
    def split(other, card0, card1):
        hand0 = Hand(other.dealer_card, other.cards[0], card0)
        hand1 = Hand(other.dealer_card, other.cards[1], card1)
        return (hand0, hand1)

    def hard_total(self):
        return sum(c for c in self.cards)

    def soft_total(self):
        return sum(c for c in self.cards)

    # This implementation of __str__ is more complex than the one
    # found in Card, as here we are dealing with a collection of
    # objects. In order to solve this, we map over the self.cards
    # collections and make each Card object a string. The final
    # result is a string of Card object
    def __str__(self):
        return ', '.join(map(str, self.cards))

    def __repr__(self):
        return f'{self.__class__.__name__}({repr(self.dealer_card)},\
                                            {", ".join(map(repr, self.cards))})'
