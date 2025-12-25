# Tic-Tac-Toe with Minimax AI

A web-based Tic-Tac-Toe game featuring an unbeatable AI opponent powered by the Minimax algorithm. Built with a FastAPI backend and a modern vanilla JavaScript frontend. Inspired by a teeko player project I did for my AI class in college.

## Overview

This project demonstrates the implementation of the Minimax algorithm for optimal game play in a classic Tic-Tac-Toe game. The AI evaluates all possible game states to make the best move, ensuring it never loses. The application features a clean RESTful API architecture and an intuitive user interface.

## Features

- **Unbeatable AI** - Implements the Minimax algorithm for optimal decision-making
- **Random Player Assignment** - Players are randomly assigned X or O at the start of each game
- **Modern UI** - Clean, responsive design with gradient backgrounds and smooth animations
- **RESTful API** - Well-structured FastAPI backend with clear endpoint separation
- **Real-time Game State** - Seamless communication between frontend and backend
- **Fast Performance** - Lightweight implementation without external dependencies

## Technologies

- **Backend**: Python 3.11+, FastAPI, Pydantic
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Algorithm**: Minimax with alpha-beta pruning principles

## Project Structure

```
tictactoe-minimax/
├── game.py          # Core game logic and Minimax algorithm implementation
├── api.py           # FastAPI backend with REST endpoints
├── index.html       # Frontend application (HTML/CSS/JavaScript)
├── requirements.txt # Python dependencies
└── README.md        # Project documentation
```

## Getting Started

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd tictactoe-minimax
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Start the backend server:
```bash
python api.py
```

The API will be available at `http://localhost:8000`

4. Open the frontend:
   - Option 1: Open `index.html` directly in your browser
   - Option 2: Serve it with a simple HTTP server:
     ```bash
     # Python 3
     python -m http.server 8080
     
     # Then navigate to http://localhost:8080
     ```

## API Documentation

### `POST /game/new`
Creates a new game instance with random player assignment.

**Response:**
```json
{
  "game_id": "123456",
  "board": [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]],
  "user_player": "X",
  "ai_player": "O",
  "status": "Your turn",
  "game_over": false
}
```

### `POST /game/{game_id}/move`
Makes a move in the current game.

**Request:**
```json
{
  "row": 0,
  "col": 1
}
```

**Response:**
```json
{
  "game_id": "123456",
  "board": [["X", "O", " "], [" ", " ", " "], [" ", " ", " "]],
  "user_player": "X",
  "ai_player": "O",
  "status": "Your turn",
  "game_over": false
}
```

### `GET /game/{game_id}`
Retrieves the current state of a game.

## Technical Implementation

### Minimax Algorithm

The Minimax algorithm is implemented in the `TicTacToe` class (`game.py`). It recursively evaluates all possible game states to determine the optimal move:

- **Maximizing player** (AI): Chooses moves that maximize the score (+1 for win)
- **Minimizing player** (Human): Chooses moves that minimize the score (-1 for loss)
- **Terminal states**: Returns +1 (AI wins), -1 (Human wins), or 0 (tie)

The algorithm explores the entire game tree, ensuring the AI never loses and will win if given the opportunity.

### Key Components

- **`minimax(is_maximizing)`**: Recursive function that evaluates game states
- **`best_move()`**: Finds the optimal move for the AI by evaluating all possibilities
- **`is_winner(player)`**: Checks for winning conditions (rows, columns, diagonals)
- **`get_available_moves()`**: Returns all valid moves for the current board state

## How It Works

1. User clicks a cell to make their move
2. Frontend sends a POST request to `/game/{game_id}/move` with the move coordinates
3. Backend validates the move and updates the game state
4. If the game continues, the AI calculates the best move using Minimax
5. The updated game state is returned to the frontend
6. The UI updates to reflect the new board state

## License

MIT License
