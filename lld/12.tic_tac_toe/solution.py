from enum import Enum
from typing import List, Optional

class Tile(Enum):
    X = "X"
    O = "O"

class GameStatus(Enum):
    IN_PROGRESS = "In Progress"
    DRAW = "Draw"
    WON = "Won"

class Player:
    def __init__(self, player_id: int, name: str, tile: Tile):
        self.player_id = player_id
        self.name = name
        self.tile = tile

    def get_move(self, board):
        # For a CLI game, ask the user for row and col
        coords = input(f"{self.name} ({self.tile.value}), enter row and col (e.g. 0 1): ")
        row, col = map(int, coords.split())
        return row, col

class Board:
    def __init__(self, size: int = 3):
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)]
        self.moves_made = 0

    def place_tile(self, row: int, col: int, tile: Tile) -> bool:
        if row < 0 or row >= self.size or col < 0 or col >= self.size or self.grid[row][col] is not None:
            return False
        self.grid[row][col] = tile
        self.moves_made += 1
        return True

    def check_winner(self, row: int, col: int, tile: Tile) -> GameStatus:
        # Check row
        if all(self.grid[row][j] == tile for j in range(self.size)):
            return GameStatus.WON
        # Check column
        if all(self.grid[i][col] == tile for i in range(self.size)):
            return GameStatus.WON
        # Check diagonal
        if row == col and all(self.grid[i][i] == tile for i in range(self.size)):
            return GameStatus.WON
        # Check anti-diagonal
        if row + col == self.size - 1 and all(self.grid[i][self.size - 1 - i] == tile for i in range(self.size)):
            return GameStatus.WON
        return GameStatus.IN_PROGRESS

    def is_full(self) -> bool:
        return self.moves_made == self.size * self.size

    def display(self):
        for r in range(self.size):
            row_str = " | ".join(cell.value if cell else " " for cell in self.grid[r])
            print(row_str)
            if r < self.size - 1:
                print("-" * (self.size * 4 - 3))
        print()

class Game:
    def __init__(self, player1: Player, player2: Player, size: int = 3):
        self.board: Board = Board(size=size)
        self.players: List[Player] = [player1, player2]
        self.current_player_index: int = 0 # Index of the current player in the players list
        self.status: GameStatus = GameStatus.IN_PROGRESS
        self.winner: Optional[Player] = None

    def start(self):
        while self.status == GameStatus.IN_PROGRESS:
            self.board.display()
            current_player = self.players[self.current_player_index]
            row, col = current_player.get_move(self.board)
            if not self.play_turn(row, col):
                continue
        self.board.display()
        if self.status == GameStatus.WON:
            print(f"Congratulations {self.winner.name}! You have won the game.")
        elif self.status == GameStatus.DRAW:
            print("The game ended in a draw.")

    def play_turn(self, row: int, col: int) -> bool:
        if self.status != GameStatus.IN_PROGRESS:
            print("Game is already over.")
            return False
        current_player = self.players[self.current_player_index]
        if not self.board.place_tile(row, col, current_player.tile):
            print("Invalid move. Try again.")
            return False
        self.status = self.board.check_winner(row, col, current_player.tile)
        if self.status == GameStatus.WON:
            self.winner = current_player
            print(f"Player {current_player.name} ({current_player.tile.value}) wins!")
        elif self.board.is_full():
            self.status = GameStatus.DRAW
            print("The game is a draw.")
        else:
            self.switch_player()

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index


# Example usage:

player1 = Player(player_id=1, name="Alice", tile=Tile.X)
player2 = Player(player_id=2, name="Bob", tile=Tile.O)
game = Game(player1, player2)
# game.play_turn(0, 0)
# game.play_turn(1, 0)
# game.play_turn(0, 1)
# game.play_turn(1, 1)
# game.play_turn(0, 2)
game.start()