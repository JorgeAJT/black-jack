# Black Jack Project in Python <span style="color:red;">♥</span> ♠ <span style="color:red;">♦</span> ♣

Welcome to the Black Jack project in Python! This project is a simple implementation of the popular card game Black Jack, developed entirely in Python.

## Description

This project simulates a game of Black Jack where the player competes against the dealer. The goal of the game is to get a hand with a value as close to 21 as possible without exceeding it, and to surpass the dealer's hand value.

## Features

- Single-player game against the dealer.
- Basic Black Jack rules.
- Interactive text-based interface.
- Clean and modular code for easy understanding and extension.

## System Requirements

- Python 3.x

## Installation

1. Clone this repository to your local machine.
   ```bash
   git clone https://github.com/yourusername/blackjack-python.git
   
2. Navigate to the project directory

   ```bash
   cd blackjack-python
   
3. (Optional) Create and activate a virtual environment.

   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   
4. Install the necessary dependencies (if any).

   ```bash
   pip install -r requirements.txt
   
## Usage

- To start the game, simply run the main.py script:

   ```bash
   python main.py

## Game Rules

1. Initial Deal: Two cards are dealt to the player and two to the dealer. One of the dealer's cards remains hidden until the end of the game.
   
2. Player's Turn: The player can choose to "Hit" (receive an additional card) or "Stand" (keep their current hand), in case it is not a straight blackjack, in that case the player win directly.
   
3. Dealer's Turn: After the player stands, the dealer reveals their hidden card and decides to "Hit" or "Stand" based on fixed rules (typically, the dealer hits on 16 or less and stands on 17 or more).
   
4. Determining the Winner:
 - If the player exceeds 21, they lose.
 - If the dealer exceeds 21, the player wins.
 - If neither exceeds 21, the hand with the lower value wins.
 - In the event of a tie, the number of cards is counted and the player with the fewest cards wins. In case of an equal number of cards, the match is considered a draw.

## Contributions

Contributions are welcome. Please follow these steps:

1. Fork the project.

2. Create a new branch with your changes:
   
   ```bash
   git checkout -b my-branch
   
3. Make your changes and commit them:
   
   ```bash
   git commit -m "Description of my changes"
   
4. Push your changes to your forked repository:
   
   ```bash
   git push origin my-branch
   
5. Create a Pull Request on GitHub.

## Author

Jorge Jiménez - JorgeAJT
