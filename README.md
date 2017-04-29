# blackjack_redux

A refactoring and revision of an early exercise:

Create a game of Blackjack that one person plays on the command line against a computer dealer, with the following rules:

The only valid moves are hit and stand.
Allow the player to play as many turns as they want.
The dealer will stand at 17 (soft or hard)
The dealer uses one deck and reshuffles after each round. The game should start the player with $100 and bets are $10. A player's turn is over when they are out of money

For my portfolio and contact information, please visit me: [Will Warren](https://willwile4.github.io)

## Objectives

* how to track state by using objects
* how to design classes to collaborate and communicate
* build an interactive game
* fundamentals of Object Oriented Programing

## How to Run

1. Install python3
2. run via CLI "$ python3 play_blackjack.py"
3. Enter your name, follow the instructions, and play blackjack!

## Files

1. blackjack.py
  - set of classes that govern game play.
  - Card, Deck, BlackjackHand, Game, Player, Dealer(Player), HumanPlayer(Player)

2. play_blackjack.py
  - UI/game play file.

3. README.md
  - This File

### Notes
- Betting seems a bit wonky at times. Need pot to carry on through a session of games, instead of one game as it is now.
