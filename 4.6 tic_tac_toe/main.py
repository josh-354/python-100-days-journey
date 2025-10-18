import sys

def print_board(board):
    """Print the Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    """Check if the player has won."""
    # Check rows, columns, diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    """Check if the board is full (draw)."""
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def tic_tac_toe():
    """Main Tic Tac Toe game function."""
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    turn = 0
    
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    
    while True:
        player = players[turn % 2]
        print(f"Player {player}'s turn.")
        
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != ' ':
                print("Invalid move. Try again.")
                continue
        except ValueError:
            print("Invalid input. Enter numbers 0-2.")
            continue
        
        board[row][col] = player
        print_board(board)
        
        if check_winner(board, player):
            print(f"Player {player} wins!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break
        
        turn += 1

if __name__ == "__main__":
    tic_tac_toe()
