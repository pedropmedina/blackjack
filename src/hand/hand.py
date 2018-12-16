# By gathering args in a single statement while initializing the
# Hand, we avoid multiple method calls which add complexity and is more
# error prompt
class Hand:
    def __init__(self, dealer_card, *args):
        self.dealer_card = dealer_card
        self.cards = list(args)

    def hard_total(self):
        return sum(c for c in self.cards)

    def soft_total(self):
        return sum(c for c in self.cards)
