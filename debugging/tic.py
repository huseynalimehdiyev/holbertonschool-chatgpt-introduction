#!/usr/bin/python3

def print_board(board):
    """
    Function: print_board
    ---------------------
    Prints the current state of the Tic-Tac-Toe board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * (len(row) * 4 - 1))  # Adjust separator dynamically


def check_winner(board):
    """
    Function: check_winner
    ----------------------
    Checks if there is a winner in the current board state.

    Returns:
    --------
    bool : True if a player has won, False otherwise
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False


def tic_tac_toe():
    """
    Function: tic_tac_toe
    ---------------------
    Runs the main Tic-Tac-Toe game loop for two players.
    """
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # Input loop with validation
        while True:
            try:
                row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
                col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
                if row not in [0, 1, 2] or col not in [0, 1, 2]:
                    print("Row and column must be 0, 1, or 2. Try again.")
                    continue
                if board[row][col] != " ":
                    print("That spot is already taken! Try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter numeric values 0, 1, or 2.")

        # Place the move
        board[row][col] = player

        # Check for winner
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")  # Correct player displayed
            break

        # Check for draw
        if all(cell != " " for row_cells in board for cell in row_cells):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        player = "O" if player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()
