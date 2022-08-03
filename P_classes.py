import random


class Player:
    cards = [[v, s] for v in ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2'] for s in ['♥', '♦', '♠', '♣']]
    random.shuffle(cards)
    comm = []
    comm_pos = []
    deck_pos = []
    pot_pos = []
    GFM_comm = []
    GFM_deck = []

    def __init__(self, name):
        self.name = name.title()
        self.in_game = "out"
        self.coins = 0
        self.hole = []
        self.did_move = "NMY"
        self.bid = 0
        self.remembered_bid = 0
        self.last_diff = 0
        self.comb_and_score = []
        self.name_and_coins_pos = []
        self.hole_A_pos = []
        self.hole_B_pos = []
        self.bid_pos = []
        self.action_pos = []
        self.token_pos = []
        self.GFM_name_and_coins = []
        self.GFM_hole = []
        self.GFM_bid = []

    def hit_hole(self):
        self.hole.append(Player.cards[0])
        del Player.cards[0]

    @classmethod
    def hit_comm(cls, num_of_cards):
        for i in range(0, num_of_cards):
            Player.comm.append(Player.cards[0])
            del Player.cards[0]


class PCPlayer(Player):
    def __init__(self, name):
        super(PCPlayer, self).__init__(name)

        self.personality = random.choice(["risker", "cautioner", "rusher", "waiter", "bluffer"])
        self.decisiveness = 0

    def hit_hole(self):
        self.hole.append(Player.cards[0])
        del Player.cards[0]

    @classmethod
    def hit_comm(cls, num_of_cards):
        for i in range(0, num_of_cards):
            Player.comm.append(Player.cards[0])
            del Player.cards[0]


class Misc:
    def __init__(self, POO, diff, diff_remembered_for_raising, min_raise, did_someone_all_in):
        self.POO = POO
        self.diff = diff
        self.diff_remembered_for_raising = diff_remembered_for_raising
        self.min_raise = min_raise
        self.did_someone_all_in = did_someone_all_in
