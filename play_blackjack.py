from blackjack import HumanPlayer, Dealer, Game, BlackjackHand, Deck
import os

def main():
    """Plays the Game"""
    os.system('clear')
    player_name = input("Please enter your name: ")
    p1 = HumanPlayer(player_name, BlackjackHand())

    print("\nWelcome to Bull City Bets - an exclusive Blackjack Casino!\n\n")

    while True:
        d1 = Dealer("dealer", BlackjackHand())
        deck = Deck()
        g = Game(p1, d1, deck)
        print("\nAnte Up!")
        p1.place_bet()
        g.add_bet()
        print("Total Pot: {} Player Purse: {}".format(g.pot, p1.purse))

        if not g.check_initial_blackjack():
            g.player_turn()
            g.dealer_turn()

        g.print_results()

        g.play_again()


if __name__ == "__main__":
    main()
