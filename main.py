board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def check_win(board):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] != ' ':
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != ' ':
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] != ' ' or board[2] == board[4] == board[6] != ' ':
        return True
    return False

def show_board():
    print(" %s | %s | %s " % (board[0], board[1], board[2]))
    print("___|___|___")
    print(" %s | %s | %s " % (board[3], board[4], board[5]))
    print("___|___|___")
    print(" %s | %s | %s " % (board[6], board[7], board[8]))
    print("   |   |   ")

show_board()

def make_move(player):
    while True:
        loc = int(input(f'Player {player}, enter where you want to make a move (1-9): ')) - 1
        if 0 <= loc <= 8 and board[loc] == ' ':
            board[loc] = player
            break
        else:
            print("Invalid move. Please select an empty cell (1-9).")

make_move('X')
show_board()

for _ in range(4):
    make_move('O')
    show_board()

    if check_win(board):
        print("Player O wins!")
        break

    make_move('X')
    show_board()

    if check_win(board):
        print("Player X wins!")
        break
else:
    print("It's a draw!")
