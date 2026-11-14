# Design a Tic-Tac-Toe game.

### Step 1: Clarify & Scope
1. **Players:** 2 human players (e.g., Player 1 with `X`, Player 2 with `O`).
2. **Board:** Single $3 \times 3$ grid (though we can store `size = 3` so it's clean).
3. **Win/Draw rules:** Standard Tic-Tac-Toe—first player to get 3 in a row (horizontally, vertically, or diagonally) wins; if all 9 cells fill up with no winner, it's a draw.

### Step 2: Trace the Core User Journeys
1. 2 players join the game & a new board is assigned.
2. While places are left and no one has won:
    * Current player (starts with X) selects a `(row, col)` and places their mark.
    * **Validate** the move (is it inside bounds and is the cell empty? If not, ask again).
    * **Check win:** Did this move give the current player 3-in-a-row? If yes $\rightarrow$ declare winner and end game.
    * **Check draw:** Are all cells full now? If yes $\rightarrow$ declare draw and end game.
    * **Switch turn** to the next player (`X` $\rightarrow$ `O`, `O` $\rightarrow$ `X`).




### Step 3 and Step 4: Extract Nouns (Data Models) & Verbs (Logic/Managers) & Write Skeleton Interfaces
- Tile(enum)
    - X
    - O
- GameStatus
    - in_progress
    - draw
    - won
- Player
    - id
    - name
    - tile: Tile
- board
    - size
    - place_tlie
    - check_winner
    - is_full
- game
    - players: List[Player]
    - board: Board
    - currnet_player_turn: int
    - status: GameStatus
    - winner: Player | None
    - play_turn

### Step 4