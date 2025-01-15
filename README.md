# Blackjack Project in Python :hearts: :clubs: :diamonds: :spades:

Welcome to the **Blackjack** project in Python! This repository contains a fully playable text-based Blackjack game, where you (the player) compete against a dealer controlled by the program.

## Table of Contents

1. Overview

2. Features

3. Project Structure

4. Requirements

5. Installation

6. Usage

7. Gameplay Rules

8. How the Code Works

9. Contributing

10. Author

## Overview
Blackjack (also known as 21) is one of the most popular casino card games. The objective is simple: get as close to **21** as possible without exceeding it, and beat the dealer’s hand.

In this Python implementation, you’ll play against a computer-controlled dealer. You start with a certain amount of money (your bank), place bets, and try to maximize your winnings while avoiding “busts” (going over 21). The game follows basic Blackjack rules with a few custom tie-break scenarios.

## Features
- **Single-player mode** against a computer dealer.
- **Variable player bank**: Choose your own starting amount.
- **Betting system**: Place bets each round, with winnings or losses updated accordingly.
- **Flexible ACE logic** for both player and dealer:
      - Player chooses whether ACE is worth 1 or 11.
      - Dealer auto-assigns ACE as 1 or 11 based on the current sum.
- **Unique tie-break rule**: If both player and dealer have the same total, the number of cards in hand decides the winner (or a true tie if they match).
- **Clear modular code** for straightforward maintenance and expansion.
- **No external libraries** required besides the Python standard library.

## Project Structure

      blackjack/
      │
      ├── main.py                # Entry point: starts the game by calling black_jack()
      │
      ├── src/
      │   ├── __init__.py
      │   ├── app.py             # Core game loop (black_jack function)
      │   └── utils/
      │       ├── __init__.py
      │       ├── card_generator.py
      │       ├── check_card.py
      │       ├── check_int_input.py
      │       ├── check_results.py
      │       ├── dealer_turn.py
      │       ├── distribute_money.py
      │       ├── generate_starting_cards.py
      │       ├── player_bet.py
      │       ├── player_turn.py
      │       └── ...

### Main Files
1. `main.py`

    - Launches the game by importing `black_jack` from `src` and executing it.

2. `src/app.py`

     - Contains the `black_jack()` function, which orchestrates the entire gameplay loop (round setup, betting, dealing cards, determining results, etc.).

3. `src/utils/*.py`

     - Collection of utility modules that handle specific tasks like generating cards, checking inputs, evaluating game results, managing bets, etc.

## Requirements

- **Python 3.x** (tested on Python 3.11+).
- No additional libraries beyond the standard library (`random`).

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/JorgeAJT/black-jack.git
   cd black-jack

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate    # Linux/Mac
   env\Scripts\activate       # Windows
3. Since there are no external Python dependencies, no `requirements.txt` is strictly needed. If you decide to create one, it might look like this:
   ```text
   # requirements.txt (example if needed)
   ```
   *(Leave it empty if no external deps.)*

4. Run the game:
   ```bash
   python main.py
   
## Usage

When you run python `main.py`, the console will guide you through each step:

1. **Enter Your Bank**: The game asks how much money you want to start with.

2. **Bet**: Each round, decide how much you want to bet.

3. **Cards Dealt**: Two cards to you and two to the dealer (one of the dealer’s cards remains hidden initially).

4. **Player Action**:
    
    - If you have an ACE, choose whether it’s worth 1 or 11.
      
    - Input `Y` to draw another card (Hit) or `N` to stand.

5. **Dealer Action**:
    
    - The dealer’s hidden card is revealed.
   
    - The dealer must follow a simple rule: hit until the total is at least 17, then stand.

6. **Results**:
    
    - If you or the dealer bust (> 21), the other side wins.
      
    - If totals tie, the number of cards each has can break the tie (fewest cards wins).
      
    - Or it’s a true tie if both have the same number of cards.

7. **Bank Updates**:
    
    - If you win, your bank increases by twice your bet.
      
    - If you lose, you forfeit your bet.
      
    - If it’s a tie, you get your bet back.

8. **Play Again or Quit**:
    
    - Continue until you run out of money or choose to stop.

## Gameplay Rules

1. **Initial Deal**:
    
    - Two cards are dealt to the player, and two cards to the dealer.
      
    - One of the dealer’s cards is hidden until the dealer’s turn.

2. **Player’s Turn**:
    
    - Check if you have a natural Blackjack (ACE + face card / 10).
      
    - Otherwise, choose “Hit” to take another card or “Stand” to hold your total.
      
    - If you exceed 21 (bust), you lose immediately.
      
3. **Dealer’s Turn**:

    - The hidden card is revealed.

    - Dealer hits until reaching a total of at least 17, then stands.

    - If the dealer exceeds 21, the dealer busts, and the player wins.

4. **Determining the Winner**:

    - If you bust, you lose.

    - If the dealer busts, you win.

    - If both totals remain ≤ 21, the higher total wins.

    - **Tie-Break**: If both totals are equal, the player with fewer cards wins. If the number of cards is also equal, it’s a true tie.

5. **Bet Resolution**:

    - Win: your bank increases by double your bet (bet * 2).

    - Lose: you lose your bet to the dealer.

    - Tie: you get your bet back.

## How the Code Works

Below is a brief overview of each utility module in `src/utils`:

- card_generator.py:
  Generates random cards (number or face card + suit) without repetition. Uses `random` from the Python standard library.
  
- `check_card.py`:

      Determines the numeric value of a card (e.g., face cards = 10, ACE = 1 or 11).
      For the dealer, ACE is chosen automatically; for the player, it prompts.

check_int_input.py:
Ensures user input for bank amount or bet is a valid integer and not greater than the current bank.

check_results.py:
Contains functions like is_blackjack(), check_player_results(), and check_general_results() to handle the logic of natural blackjack, busts, ties, and final outcomes.

dealer_turn.py:
Implements the dealer’s logic. The dealer draws cards until reaching at least 17.

player_turn.py:
Handles the player’s actions, including deciding whether to take extra cards or stand.

player_bet.py:
Deducts the player’s chosen bet from their bank.

distribute_money.py:
Updates both the player’s and dealer’s bank after each round based on the result.

generate_starting_cards.py:
Draws the initial four cards (two for the player and two for the dealer).

app.py (called by black_jack()):

Manages the game loop, rounds, and transitions between the different functions above.
Contributing
Contributions are very welcome! If you have ideas for improvements or bug fixes:

Fork the repository.
Create a new branch:
bash
Copiar código
git checkout -b my-new-feature
Make changes and commit:
bash
Copiar código
git commit -m "Add new feature or fix bug"
Push to your fork:
bash
Copiar código
git push origin my-new-feature
Create a Pull Request on GitHub and wait for review.
Author
Jorge Jiménez – JorgeAJT
Feel free to reach out if you have any questions or suggestions!
