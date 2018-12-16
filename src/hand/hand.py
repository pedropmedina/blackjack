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

    def __str__(self):
        return ', '.join(map(str, self.cards))

    def hard_total(self):
        return sum(c for c in self.cards)

    def soft_total(self):
        return sum(c for c in self.cards)
