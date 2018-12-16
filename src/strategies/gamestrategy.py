# Strategy objects are pluggled into a Master obejct to implement
# the algorithm logic.
# They is more likely to have no data of its own (stateless)
# They follow the Flyweight design patter avoiding internal storage.
# All values are provided as method arguments.


class GameStrategy:
    def insurance(self, hand):
        return False

    def split(self, hand):
        return False

    def double(self, hand):
        return False

    def hit(self, hand):
        return sum(c.hard for c in hand.cards) <= 17
