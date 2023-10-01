# Initialize a 3x3 empty board
board = [[" " for _ in range(3)] for _ in range(3)]

# Function to display the Tic Tac Toe board


def print_board(board):
    for row in board:
        print(" | ".join(row))
        if row != board[-1]:
            print("-" * 9)

# Function to check if the board is full


def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

# Function to check if someone has won the game


def is_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
            all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

# Function to evaluate the current state of the board


def evaluate(board):
    if is_winner(board, "X"):
        return 1
    elif is_winner(board, "O"):
        return -1
    elif is_board_full(board):
        return 0
    else:
        return None

# Minimax algorithm


def minimax(board, depth, maximizing_player):
    result = evaluate(board)

    if result is not None:
        return result

    if maximizing_player:
        max_eval = -float("inf")
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "X"
                    eval = minimax(board, depth + 1, False)
                    board[row][col] = " "
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "O"
                    eval = minimax(board, depth + 1, True)
                    board[row][col] = " "
                    min_eval = min(min_eval, eval)
        return min_eval

# Function to make the best move for the AI (X)


def best_move(board):
    best_eval = -float("inf")
    best_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = "X"
                eval = minimax(board, 0, False)
                board[row][col] = " "
                if eval > best_eval:
                    best_eval = eval
                    best_move = (row, col)
    return best_move


# Main game loop
while True:
    print_board(board)

    # Player's turn
    while True:
        try:
            row, col = map(int, input(
                "Enter your move (row and column, e.g., 0 1): ").split())
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                board[row][col] = "O"
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter row and column as integers.")

    if is_winner(board, "O"):
        print_board(board)
        print("You win!")
        break

    if is_board_full(board):
        print_board(board)
        print("It's a draw!")
        break

    # AI's turn
    ai_move = best_move(board)
    board[ai_move[0]][ai_move[1]] = "X"

    if is_winner(board, "X"):
        print_board(board)
        print("AI wins!")
        break

    if is_board_full(board):
        print_board(board)
        print("It's a draw!")
        break
