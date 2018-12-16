from ..deck.deck import Deck
from ..hand.hand import Hand

# The Table class interacts with event from the Player instance
# 1. The player places initial bet based on betting strategy
# 2. The player receives a hand
# 3. The player's hand is splittable The player must decide to
# split or not which can create additional Hand
# 4. For each Hand instance, the player must decide to hit, double, or
# stand based on play strategy
# 5. The player, then receives a payout, and must update betting based
# on wins or losses

d = Deck()


class Table:
    def __init__(self):
        self.deck = Deck()

    def place_bet(self, amount):
        print('Bet', amount)

    def get_hand(self):
        try:
            self.hand = Hand(d.pop(), d.pop(), d.pop())
            self.hole_card = d.pop()
        except IndexError:
            # Out of cards: need to shuffle
            self.deck = Deck()
            return self.get_hand()
        print('Deal', self.hand)
        return self.hand

    def get_insurance(self, hand):
        return hand.dealer_card.insure
