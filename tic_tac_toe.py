# Simple CLI-based Tic Tac Toe game made using Python 🐍
# To be honest, Python 🐍 is very fun to code in!!

class TicTacToe:
    def __init__(self):
        self.board = [[' '] * 3 for _ in range(3)]
        self.current_player = 'X'
        self.moves_made = 0
    
    def display_board(self):
        print("\n   0   1   2")
        for i, row in enumerate(self.board):
            print(f"{i}  {' | '.join(row)}")
            if i < 2:
                print("  -----------")
    
    def is_valid_move(self, row, col):
        return 0 <= row <= 2 and 0 <= col <= 2 and self.board[row][col] == ' '
    
    def make_move(self, row, col):
        if self.is_valid_move(row, col):
            self.board[row][col] = self.current_player
            self.moves_made += 1
            return True
        return False
    
    def check_winner(self):
        # Check rows and columns
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        
        return None
    
    def is_board_full(self):
        return self.moves_made == 9
    
    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def get_player_move(self):
        while True:
            try:
                move = input(f"Player {self.current_player}, enter row,col (0-2): ")
                row, col = map(int, move.split(','))
                return row, col
            except ValueError:
                print("Invalid format! Use: row,col (e.g., 1,2)")
    
    def play(self):
        print("Welcome to Tic-Tac-Toe!")
        print("Enter moves as row,col (e.g., 1,2)")
        
        while True:
            self.display_board()
            row, col = self.get_player_move()
            
            if self.make_move(row, col):
                winner = self.check_winner()
                if winner:
                    self.display_board()
                    print(f"\nPlayer {winner} wins!")
                    break
                
                if self.is_board_full():
                    self.display_board()
                    print("\nIt's a tie!")
                    break
                
                self.switch_player()
            else:
                print("Invalid move! Try again.")

# Run the game
if __name__ == "__main__":
    game = TicTacToe()
    game.play()
