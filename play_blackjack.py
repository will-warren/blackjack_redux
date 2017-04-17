from blackjack import HumanPlayer, Dealer, Game, BlackjackHand, Deck
import os

def main():
    """Plays the Game"""
    os.system('clear')
    player_name = input("Please enter your name: ")

    print("\nWelcome to Bull City Bets - an exclusive Blackjack Casino!\n\n")

    while True:
        p1 = HumanPlayer(player_name, BlackjackHand())
        d1 = Dealer("dealer", BlackjackHand())
        deck = Deck()
        g = Game(p1, d1, deck)
        print("Ante Up!")
        p1.place_bet()
        g.add_bet()
        print("Total Pot: {} Player Purse: {}".format(g.pot, p1.purse))

        if not g.check_initial_blackjack():
            g.player_turn()
            g.dealer_turn()

        g.print_results()

        if not input("play again? "):
            return


if __name__ == "__main__":
    main()
