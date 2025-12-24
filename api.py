from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
from game import TicTacToe
import random

app = FastAPI(title="Tic-Tac-Toe API")

# Enable CORS for frontend
# Allow localhost for development and portfolio domain for production
import os
allowed_origins = os.getenv("ALLOWED_ORIGINS", "*").split(",") if os.getenv("ALLOWED_ORIGINS") else [
    "http://localhost:8080",
    "http://localhost:3000",
    "http://127.0.0.1:8080",
    "http://127.0.0.1:3000",
    "https://sidvalecha.com",
    "https://www.sidvalecha.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Game state storage (in production, use Redis or database)
# Format: {game_id: {'game': TicTacToe, 'user_player': 'X', 'ai_player': 'O'}}
games = {}

class GameState(BaseModel):
    board: List[List[str]]
    user_player: str
    ai_player: str
    status: str

class MoveRequest(BaseModel):
    row: int
    col: int

class GameResponse(BaseModel):
    game_id: str
    board: List[List[str]]
    user_player: str
    ai_player: str
    status: str
    game_over: bool

@app.get("/")
def root():
    return {"message": "Tic-Tac-Toe API"}

@app.post("/game/new", response_model=GameResponse)
def new_game():
    """Create a new game with random player assignment"""
    game_id = str(random.randint(100000, 999999))
    user_player = random.choice(['X', 'O'])
    ai_player = 'O' if user_player == 'X' else 'X'
    
    game = TicTacToe(ai_player=ai_player)
    
    # If user is O, AI makes first move
    if user_player == 'O':
        ai_move = game.best_move()
        if ai_move:
            game.board[ai_move[0]][ai_move[1]] = ai_player
    
    games[game_id] = {
        'game': game,
        'user_player': user_player,
        'ai_player': ai_player
    }
    
    status = "Your turn"
    if user_player == 'O' and game.is_winner(ai_player):
        status = "AI wins! 🤖"
    elif game.is_full():
        status = "It's a tie!"
    
    game_over = game.is_winner(user_player) or game.is_winner(ai_player) or game.is_full()
    
    return GameResponse(
        game_id=game_id,
        board=game.board,
        user_player=user_player,
        ai_player=ai_player,
        status=status,
        game_over=game_over
    )

@app.post("/game/{game_id}/move", response_model=GameResponse)
def make_move(game_id: str, move: MoveRequest):
    """Make a move in the game"""
    if game_id not in games:
        raise HTTPException(status_code=404, detail="Game not found")
    
    game_data = games[game_id]
    game = game_data['game']
    user_player = game_data['user_player']
    ai_player = game_data['ai_player']
    
    # Validate move
    if move.row < 0 or move.row > 2 or move.col < 0 or move.col > 2:
        raise HTTPException(status_code=400, detail="Invalid move coordinates")
    
    if game.board[move.row][move.col] != ' ':
        raise HTTPException(status_code=400, detail="Cell already occupied")
    
    # Check if game is over
    if game.is_winner(user_player) or game.is_winner(ai_player) or game.is_full():
        raise HTTPException(status_code=400, detail="Game is over")
    
    # User move
    game.board[move.row][move.col] = user_player
    
    status = "Your turn"
    game_over = False
    
    # Check if user wins
    if game.is_winner(user_player):
        status = "You win! 🎉"
        game_over = True
    elif game.is_full():
        status = "It's a tie!"
        game_over = True
    else:
        # AI move
        ai_move = game.best_move()
        if ai_move:
            game.board[ai_move[0]][ai_move[1]] = ai_player
            
            if game.is_winner(ai_player):
                status = "AI wins! 🤖"
                game_over = True
            elif game.is_full():
                status = "It's a tie!"
                game_over = True
    
    return GameResponse(
        game_id=game_id,
        board=game.board,
        user_player=user_player,
        ai_player=ai_player,
        status=status,
        game_over=game_over
    )

@app.get("/game/{game_id}", response_model=GameResponse)
def get_game(game_id: str):
    """Get current game state"""
    if game_id not in games:
        raise HTTPException(status_code=404, detail="Game not found")
    
    game_data = games[game_id]
    game = game_data['game']
    user_player = game_data['user_player']
    ai_player = game_data['ai_player']
    
    status = "Your turn"
    if game.is_winner(user_player):
        status = "You win! 🎉"
    elif game.is_winner(ai_player):
        status = "AI wins! 🤖"
    elif game.is_full():
        status = "It's a tie!"
    
    return GameResponse(
        game_id=game_id,
        board=game.board,
        user_player=user_player,
        ai_player=ai_player,
        status=status,
        game_over=game.is_winner(user_player) or game.is_winner(ai_player) or game.is_full()
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

