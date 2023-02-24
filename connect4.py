import numpy as np

def create_board(rows, cols):
    # Creates a new board with the given number of rows and columns.
    return np.zeros((rows, cols), dtype=int)

def drop_piece(board, row, col, piece):
    # Drops a piece (1 or 2) in the specified column on the board.
    board[row][col] = piece

def is_valid_location(board, col):
    # Checks if the specified column on the board is a valid location to drop a piece.
    return board[0][col] == 0

def get_next_open_row(board, col):
    # Returns the next open row in the specified column on the board.
    for r in range(rows-1, -1, -1):
        if board[r][col] == 0:
            return r

def print_board(board):
    # Prints the current state of the board.
    print(np.flip(board, 0))

def winning_move(board, piece):
    # Checks if the specified piece has won the game.
    # Check for horizontal win
    for c in range(cols - 3):
        for r in range(rows):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check for vertical win
    for c in range(cols):
        for r in range(rows - 3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check for diagonal win (positive slope)
    for c in range(cols - 3):
        for r in range(rows - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check for diagonal win (negative slope)
    for c in range(cols - 3):
        for r in range(3, rows):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

    return False

# Get board size from user input
while True:
    try:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

# Initialize board and starting player
board = create_board(rows, cols)
player = 1

# Play game
game_over = False
while not game_over:
    # Get player input
    while True:
        try:
            col = int(input("Player " + str(player) + ", choose a column (0-" + str(cols-1) + "): "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Drop piece in the selected column
    if is_valid_location(board, col):
        row = get_next_open_row(board, col)
        drop_piece(board, row, col, player)

        # Check if the move won the game
        if winning_move(board, player):
            print("Player " + str(player) + " wins!")
            game_over = True

        # Switch to the
