class Player:
    def __init__(self, table, bet_strategy, game_strategy, **kwargs):
        self.bet_strategy = bet_strategy
        self.game_strategy = game_strategy
        self.table = table
        self.__dict__.update(kwargs)

    def game(self):
        self.table.place_bet(self.bet_strategy.bet())
        self.hand = self.table.get_hand()
        if self.table.can_insure(self.hand):
            if self.game_strategy.insurance(self.hand):
                self.table.insurance(self.bet_strategy.bet())
