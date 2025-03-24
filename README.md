# Tic-Tac-Toe with Minimax AI

## Overview
This project implements a Tic-Tac-Toe game where a human player competes against an AI opponent using the Minimax algorithm. The AI plays optimally, ensuring the best possible move at every turn.

## Features
- **Board Representation**: A 3x3 grid.
- **Win Checking**: Detects row, column, and diagonal wins.
- **Minimax Algorithm**: Ensures the AI plays optimally.
- **Interactive Gameplay**: Allows a human player to play against the AI.
- **Automatic AI Moves**: The AI calculates and plays its move instantly after the player.

## How It Works
1. The game starts with an empty board.
2. The human player ('O') makes a move by entering row and column indices (0-2).
3. The AI ('X') calculates the best move using the Minimax algorithm.
4. The game continues until:
   - A player wins by forming a row, column, or diagonal.
   - The board is full, resulting in a tie.
5. The winner or tie is displayed, and the game ends.

## Installation
1. Ensure you have Python installed (version 3.x recommended).
2. Clone or download this repository.
3. Run the script using:
   ```sh
   python tic_tac_toe.py
   ```

## Usage
- When prompted, enter your move in the format: `row column` (e.g., `1 2` for row 1, column 2).
- The AI will play automatically after your move.
- The game will display the board after each turn.
- The game ends when there is a winner or a tie.

## Algorithm - Minimax
The AI uses the **Minimax algorithm** to evaluate all possible moves and choose the best one. The algorithm:
- Recursively evaluates possible board states.
- Assigns scores: `+1` for AI wins, `-1` for human wins, `0` for ties.
- Chooses the move that minimizes the opponent's best outcome while maximizing its own.

## Possible Enhancements
- **Alpha-Beta Pruning**: Optimize Minimax by pruning unnecessary branches.
- **GUI Integration**: Implement a graphical version using Pygame or Tkinter.
- **Difficulty Levels**: Add varying levels by adjusting the Minimax depth.


## Author
Sid Valecha

