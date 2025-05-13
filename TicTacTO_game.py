import random

# Define the game board
board = [" " for _ in range(9)]

def print_board():
    for i in range(3):
        print("|".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-" * 5)

# Check for a win
def check_win(player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

# Check for tie
def check_tie():
    return " " not in board

# Player move
def player_move():
    while True:
        try:
            move = int(input("Choose a position (1-9): ")) - 1
            if 0 <= move < 9 and board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")

# AI move
def ai_move():
    available_moves = [i for i in range(9) if board[i] == " "]
    move = random.choice(available_moves)
    board[move] = "O"

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()

    while True:
        player_move()
        print_board()
        if check_win("X"):
            print("You win!")
            break
        if check_tie():
            print("It's a tie!")
            break

        print("AI's turn...")
        ai_move()
        print_board()
        if check_win("O"):
            print("AI wins!")
            break
        if check_tie():
            print("It's a tie!")
            break

# Start the game
if __name__ == "__main__":
    play_game()
