from src.deck.deck import Deck
from src.hand.hand import Hand

deck = Deck()
hand = Hand(deck.pop(), deck.pop(), deck.pop())

print(hand.cards)
