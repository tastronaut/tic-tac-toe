import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WINDOW_SIZE = 600
GRID_SIZE = 3
CELL_SIZE = WINDOW_SIZE // GRID_SIZE
LINE_WIDTH = 5
SYMBOL_WIDTH = 8
SYMBOL_MARGIN = 50

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
LIGHT_GRAY = (200, 200, 200)
BLUE = (0, 100, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class TicTacToeGUI:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
        pygame.display.set_caption("Tic-Tac-Toe")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 80)
        self.small_font = pygame.font.Font(None, 36)
        
        # Game state
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
        self.winner = None
        self.winning_line = None
        
    def draw_grid(self):
        """Draw the tic-tac-toe grid"""
        for i in range(1, GRID_SIZE):
            # Vertical lines
            pygame.draw.line(self.screen, BLACK, 
                           (i * CELL_SIZE, 0), 
                           (i * CELL_SIZE, WINDOW_SIZE), 
                           LINE_WIDTH)
            # Horizontal lines
            pygame.draw.line(self.screen, BLACK, 
                           (0, i * CELL_SIZE), 
                           (WINDOW_SIZE, i * CELL_SIZE), 
                           LINE_WIDTH)
    
    def draw_symbols(self):
        """Draw X and O symbols on the board"""
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == 'X':
                    self.draw_x(row, col)
                elif self.board[row][col] == 'O':
                    self.draw_o(row, col)
    
    def draw_x(self, row, col):
        """Draw X symbol in the specified cell"""
        center_x = col * CELL_SIZE + CELL_SIZE // 2
        center_y = row * CELL_SIZE + CELL_SIZE // 2
        
        # Draw X as two diagonal lines
        pygame.draw.line(self.screen, RED,
                        (center_x - SYMBOL_MARGIN, center_y - SYMBOL_MARGIN),
                        (center_x + SYMBOL_MARGIN, center_y + SYMBOL_MARGIN),
                        SYMBOL_WIDTH)
        pygame.draw.line(self.screen, RED,
                        (center_x + SYMBOL_MARGIN, center_y - SYMBOL_MARGIN),
                        (center_x - SYMBOL_MARGIN, center_y + SYMBOL_MARGIN),
                        SYMBOL_WIDTH)
    
    def draw_o(self, row, col):
        """Draw O symbol in the specified cell"""
        center_x = col * CELL_SIZE + CELL_SIZE // 2
        center_y = row * CELL_SIZE + CELL_SIZE // 2
        
        # Draw O as a circle
        pygame.draw.circle(self.screen, BLUE, 
                          (center_x, center_y), 
                          SYMBOL_MARGIN, 
                          SYMBOL_WIDTH)
    
    def get_cell_from_pos(self, pos):
        """Convert mouse position to board coordinates"""
        x, y = pos
        row = y // CELL_SIZE
        col = x // CELL_SIZE
        return row, col
    
    def is_valid_move(self, row, col):
        """Check if move is valid"""
        return (0 <= row < 3 and 0 <= col < 3 and 
                self.board[row][col] == '' and not self.game_over)
    
    def make_move(self, row, col):
        """Make a move on the board"""
        if self.is_valid_move(row, col):
            self.board[row][col] = self.current_player
            
            # Check for winner
            if self.check_winner():
                self.game_over = True
                self.winner = self.current_player
            elif self.is_board_full():
                self.game_over = True
                self.winner = 'Tie'
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def check_winner(self):
        """Check if there's a winner and store winning line"""
        # Check rows
        for row in range(3):
            if (self.board[row][0] == self.board[row][1] == self.board[row][2] != ''):
                self.winning_line = ('row', row)
                return True
        
        # Check columns
        for col in range(3):
            if (self.board[0][col] == self.board[1][col] == self.board[2][col] != ''):
                self.winning_line = ('col', col)
                return True
        
        # Check diagonals
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] != ''):
            self.winning_line = ('diag', 0)
            return True
        if (self.board[0][2] == self.board[1][1] == self.board[2][0] != ''):
            self.winning_line = ('diag', 1)
            return True
        
        return False
    
    def is_board_full(self):
        """Check if board is full"""
        for row in self.board:
            if '' in row:
                return False
        return True
    
    def draw_winning_line(self):
        """Draw line through winning combination"""
        if not self.winning_line:
            return
        
        line_type, index = self.winning_line
        
        if line_type == 'row':
            start_pos = (0, index * CELL_SIZE + CELL_SIZE // 2)
            end_pos = (WINDOW_SIZE, index * CELL_SIZE + CELL_SIZE // 2)
        elif line_type == 'col':
            start_pos = (index * CELL_SIZE + CELL_SIZE // 2, 0)
            end_pos = (index * CELL_SIZE + CELL_SIZE // 2, WINDOW_SIZE)
        elif line_type == 'diag':
            if index == 0:  # Main diagonal
                start_pos = (0, 0)
                end_pos = (WINDOW_SIZE, WINDOW_SIZE)
            else:  # Anti-diagonal
                start_pos = (WINDOW_SIZE, 0)
                end_pos = (0, WINDOW_SIZE)
        
        pygame.draw.line(self.screen, GREEN, start_pos, end_pos, LINE_WIDTH * 2)
    
    def draw_game_status(self):
        """Draw current game status"""
        if self.game_over:
            if self.winner == 'Tie':
                text = "It's a Tie!"
                color = GRAY
            else:
                text = f"Player {self.winner} Wins!"
                color = RED if self.winner == 'X' else BLUE
            
            restart_text = "Press R to restart"
            
            # Draw semi-transparent overlay
            overlay = pygame.Surface((WINDOW_SIZE, WINDOW_SIZE))
            overlay.set_alpha(128)
            overlay.fill(WHITE)
            self.screen.blit(overlay, (0, 0))
            
            # Draw winner text
            winner_surface = self.font.render(text, True, color)
            winner_rect = winner_surface.get_rect(center=(WINDOW_SIZE//2, WINDOW_SIZE//2 - 50))
            self.screen.blit(winner_surface, winner_rect)
            
            # Draw restart text
            restart_surface = self.small_font.render(restart_text, True, BLACK)
            restart_rect = restart_surface.get_rect(center=(WINDOW_SIZE//2, WINDOW_SIZE//2 + 50))
            self.screen.blit(restart_surface, restart_rect)
        else:
            # Draw current player
            text = f"Player {self.current_player}'s Turn"
            color = RED if self.current_player == 'X' else BLUE
            
            player_surface = self.small_font.render(text, True, color)
            player_rect = player_surface.get_rect(center=(WINDOW_SIZE//2, 30))
            self.screen.blit(player_surface, player_rect)
    
    def reset_game(self):
        """Reset the game to initial state"""
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
        self.winner = None
        self.winning_line = None
    
    def handle_events(self):
        """Handle pygame events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and not self.game_over:  # Left click
                    row, col = self.get_cell_from_pos(event.pos)
                    self.make_move(row, col)
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # R key to restart
                    self.reset_game()
                elif event.key == pygame.K_ESCAPE:  # ESC to quit
                    return False
        
        return True
    
    def draw(self):
        """Draw everything on the screen"""
        self.screen.fill(WHITE)
        self.draw_grid()
        self.draw_symbols()
        
        if self.game_over and self.winner != 'Tie':
            self.draw_winning_line()
        
        self.draw_game_status()
        pygame.display.flip()
    
    def run(self):
        """Main game loop"""
        running = True
        while running:
            running = self.handle_events()
            self.draw()
            self.clock.tick(60)  # 60 FPS
        
        pygame.quit()
        sys.exit()

# Run the game
if __name__ == "__main__":
    game = TicTacToeGUI()
    game.run()
