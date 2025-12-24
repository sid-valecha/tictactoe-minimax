# Tic-Tac-Toe with Minimax AI

A web-based Tic-Tac-Toe game with an unbeatable AI using the Minimax algorithm. Built with FastAPI backend and vanilla HTML/CSS/JavaScript frontend.

## Features

- ✅ **Unbeatable AI** - Uses Minimax algorithm for optimal play
- ✅ **Random Player Assignment** - Randomly assigns X or O to the user
- ✅ **Beautiful UI** - Modern gradient design with red X and black O
- ✅ **Fast Performance** - FastAPI backend (no Pyodide overhead)
- ✅ **RESTful API** - Clean API design for game state management

## Project Structure

```
tictactoe-minimax/
├── game.py          # Core game logic with Minimax algorithm
├── api.py           # FastAPI backend
├── index.html       # Frontend (HTML/CSS/JS)
├── requirements.txt # Python dependencies
└── README.md        # This file
```

## Local Development

### Backend (API)

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the API server:
```bash
python api.py
# or
uvicorn api:app --reload
```

The API will be available at `http://localhost:8000`

### Frontend

1. Open `index.html` in your browser, or serve it with a simple HTTP server:
```bash
# Python 3
python -m http.server 8080

# Node.js (if you have http-server installed)
npx http-server -p 8080
```

2. Update the `API_BASE_URL` in `index.html` if needed (defaults to `http://localhost:8000` for local development)

3. Open `http://localhost:8080` in your browser

## API Endpoints

### `POST /game/new`
Create a new game with random player assignment.

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
Make a move in the game.

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
Get current game state.

## Deployment

### Backend Deployment (FastAPI)

#### Option 1: Heroku

1. Create a `Procfile`:
```
web: uvicorn api:app --host 0.0.0.0 --port $PORT
```

2. Create `runtime.txt`:
```
python-3.11.0
```

3. Deploy:
```bash
heroku create your-app-name
git push heroku main
```

#### Option 2: Railway

1. Connect your GitHub repo to Railway
2. Railway will auto-detect FastAPI and deploy
3. Update `API_BASE_URL` in `index.html` with Railway URL

#### Option 3: Render

1. Create a new Web Service
2. Set build command: `pip install -r requirements.txt`
3. Set start command: `uvicorn api:app --host 0.0.0.0 --port $PORT`
4. Deploy

### Frontend Deployment (Netlify)

1. Go to [Netlify Drop](https://app.netlify.com/drop)
2. Drag and drop `index.html`
3. Update `API_BASE_URL` in `index.html` to your deployed API URL
4. Redeploy

Or use Git:
1. Push to GitHub
2. Connect to Netlify
3. Set build command: (empty)
4. Set publish directory: (empty)
5. Add environment variable or update `API_BASE_URL` in code

## Environment Variables

For production, you may want to set:
- `API_URL` - Your deployed API URL (update in `index.html`)

## CORS

The API currently allows all origins (`allow_origins=["*"]`). For production, update this in `api.py`:

```python
allow_origins=["https://your-frontend-domain.com"]
```

## Game Logic

The Minimax algorithm is implemented in `game.py`:
- `minimax()` - Recursive algorithm to evaluate all possible moves
- `best_move()` - Finds the optimal move for the AI
- Returns +1 for AI win, -1 for human win, 0 for tie

## License

MIT
