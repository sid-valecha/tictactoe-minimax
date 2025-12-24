import math

class TicTacToe:
    def __init__(self, ai_player='O'):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.ai_player = ai_player  # 'X' or 'O'
        self.human_player = 'O' if ai_player == 'X' else 'X'

    def is_winner(self, player):
        # Check rows, columns, and diagonals
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or \
               all(self.board[j][i] == player for j in range(3)):
                return True
        
        if all(self.board[i][i] == player for i in range(3)) or \
           all(self.board[i][2 - i] == player for i in range(3)):
            return True
        
        return False

    def is_full(self):
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))

    def get_available_moves(self):
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ' ']

    def minimax(self, is_maximizing):
        if self.is_winner(self.ai_player):  # AI wins
            return 1
        if self.is_winner(self.human_player):  # Human wins
            return -1
        if self.is_full():
            return 0

        if is_maximizing:
            best_score = -math.inf
            for (i, j) in self.get_available_moves():
                self.board[i][j] = self.ai_player
                score = self.minimax(False)
                self.board[i][j] = ' '
                best_score = max(best_score, score)
            return best_score
        else:
            best_score = math.inf
            for (i, j) in self.get_available_moves():
                self.board[i][j] = self.human_player
                score = self.minimax(True)
                self.board[i][j] = ' '
                best_score = min(best_score, score)
            return best_score

    def best_move(self):
        best_score = -math.inf
        move = None
        for (i, j) in self.get_available_moves():
            self.board[i][j] = self.ai_player
            score = self.minimax(False)
            self.board[i][j] = ' '
            if score > best_score:
                best_score = score
                move = (i, j)
        return move
