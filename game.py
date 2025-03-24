import math

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

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
        if self.is_winner('X'):
            return 1
        if self.is_winner('O'):
            return -1
        if self.is_full():
            return 0

        if is_maximizing:
            best_score = -math.inf
            for (i, j) in self.get_available_moves():
                self.board[i][j] = 'X'
                score = self.minimax(False)
                self.board[i][j] = ' '
                best_score = max(best_score, score)
            return best_score
        else:
            best_score = math.inf
            for (i, j) in self.get_available_moves():
                self.board[i][j] = 'O'
                score = self.minimax(True)
                self.board[i][j] = ' '
                best_score = min(best_score, score)
            return best_score

    def best_move(self):
        best_score = -math.inf
        move = None
        for (i, j) in self.get_available_moves():
            self.board[i][j] = 'X'
            score = self.minimax(False)
            self.board[i][j] = ' '
            if score > best_score:
                best_score = score
                move = (i, j)
        return move

    def play(self):
        while True:
            self.print_board()
            if self.is_winner('X'):
                print("AI wins!")
                break
            if self.is_winner('O'):
                print("You win!")
                break
            if self.is_full():
                print("It's a tie!")
                break
            
            # Human move
            row, col = map(int, input("Enter row and column (0-2): ").split())
            if self.board[row][col] == ' ':
                self.board[row][col] = 'O'
            else:
                print("Invalid move! Try again.")
                continue
            
            if not self.is_full():
                ai_move = self.best_move()
                self.board[ai_move[0]][ai_move[1]] = 'X'

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
