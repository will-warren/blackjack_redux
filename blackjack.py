import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return "{}{}".format(self.rank, self.suit[0].upper())

    def short_name(self):
        """givs an abbreviated name for a card"""
        return "{}{}".format(self.rank, self.suit[0].upper())

    def long_name(self):
        """gives long name (letters) for card's value and suit"""
        value_translations = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",7: "seven", 8: "eight", 9: "nine",
        10: "ten", 'J': "Jack", "Q": "Queen", "K": "King", "A":"Ace"}
        return "{} of {}".format(value_translations[self.rank], self.suit)

    def card_down(self):
        """shows the card face down on the table"""
        return "??"

    def __eq__(self, other):
        return self.value == other.value and self.suit == other.suit


class Deck:
    def __init__(self): #, deck_list):
        all_ranks_list = [2,3,4,5,6,7,8,9,10,'J','Q',"K","A"]
        all_suits_list = ["hearts", "spades", "diamonds", "clubs"]
        self.deck = [Card(rank, suit) for suit in all_suits_list for rank in all_ranks_list]
        # self.deck = deck_list

    def __repr__(self):
        """repr as all the cards in one deck, uses card method"""
        for card in self.deck:
            return card.short_name()

    #
    # def __str__(self):
    #     return __repr__()

    def shuffle_deck(self):
        """shuffles the deck"""
        random.shuffle(self.deck)
        # return self.deck

    def deal_card(self):
        """deals one card from the deck"""
        if len(self.deck):
            return self.deck.pop(0)
        else:
            raise Error


class BlackjackHand:
    def __init__(self):
        self.hand = []

    def __repr__(self):
        return str([card.short_name() for card in self.hand])

    def add_card_to_hand(self, Card):
        """adds card to hand"""
        self.hand.append(Card)

    def compute_score(self):
        """totals up the score for a hand"""
        score = 0
        ace_count = 0
        for card in self.hand:
            if isinstance(card.rank, int):
                score += card.rank
            elif card.rank == "A":
                score += 11
                ace_count += 1
            else:
                score += 10
        while ace_count > 0 and score > 21:
            score -= 10
            ace_count -= 1
        return score

    def new_hand(self):
        self.hand = []


class Game:
    def __init__(self, player, dealer, deck):
        self.player = player
        self.dealer = dealer
        self.game_deck = Deck()
        self.game_deck.shuffle_deck()
        self.pot = 0

        for _ in range(2):
            print(self.game_deck)
            self.player.take_card(self.game_deck.deal_card())
            self.dealer.take_card(self.game_deck.deal_card())

    def player_turn(self):
        while not self.game_over() and self.player.hit():
            self.player.take_card(self.game_deck.deal_card())
            print(self.player.hand)

    def dealer_turn(self):
        while not self.game_over() and self.dealer.hit():
            self.dealer.take_card(self.game_deck.deal_card())

    def __repr__(self):
        return "This is a Game between {} and {}".format(self.player.name, self.dealer.name)

    def game_over(self):
        # what are the conditions?  player bust, player stand, dealer bust, dealer stand
        return (self.player.hand.compute_score() > 21 or
                self.dealer.hand.compute_score() > 21 or
                self.dealer.stood)

    def play_again(self):
        play_again = input("\nDo you want to play again? [ Y / anything else to quit]   ").upper()
        if play_again[0] == 'Y':
            self.pot = 0
            return True
        else:
            exit()

    def print_results(self):
        print("player hand", self.player.hand, self.player.hand.compute_score())
        print("dealer hand", self.dealer.hand, self.dealer.hand.compute_score())
        if self.player.hand.compute_score() > 21:
            print("player busts")
            self.player.hand.new_hand()
            return
        if self.dealer.hand.compute_score() > 21:
            print("dealer busts")
            self.player.blackjack_bet(self.pot)
            self.player.hand.new_hand()
            return
        if self.player.hand.compute_score() > self.dealer.hand.compute_score():
            print("player wins")
            self.player.winning_bet(self.pot)
            self.player.hand.new_hand()
            return
        if self.player.hand.compute_score() == self.dealer.hand.compute_score():
            print("push")
            self.player.push()
            self.player.hand.new_hand()
            return
        print("dealer wins")
        self.player.hand.new_hand()

    def check_initial_blackjack(self):
        s1 = self.player.hand.compute_score()
        s2 = self.dealer.hand.compute_score()
        if s1 == 21 or s2 == 21:
            return True
        else:
            return False

    def add_bet(self):
        self.pot += 10


class Player:
    def __init__(self, name, blackjackhand):
        self.hand = blackjackhand
        self.name = name
        self.stood = False

    def take_card(self, card):
        self.hand.add_card_to_hand(card)


class Dealer(Player):
    def hit(self):
        self.stood = self.hand.compute_score() < 17
        return self.stood


class HumanPlayer(Player):
    def __init__(self, name, blackjackhand):
        super().__init__(name, blackjackhand)
        self.purse = 100
        self.bet = 10

    def hit(self):
        self.stood = input("would you like to hit or stand? h/s ") == "h"
        return self.stood


    def place_bet(self):
        if self.purse >= 10:
            self.purse -= self.bet
        else:
            print("You are out of money, and the game is over")
            Game.game_over(self, self.name)

    def winning_bet(self, total_pot):
        self.purse += total_pot

    def blackjack_bet(self, total_pot):
        # player keeps their money and gets $15 from the dealer
        self.purse += (total_pot + 15)

    def push(self):
        self.purse += self.bet
