import random
import time

# function to show the board
def draw_board(board):
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()

# check if someone won
def check_winner(board):
    win_positions = [
        (0,1,2),(3,4,5),(6,7,8), # rows
        (0,3,6),(1,4,7),(2,5,8), # columns
        (0,4,8),(2,4,6)          # diagonals
    ]
    for x, y, z in win_positions:
        if board[x] == board[y] == board[z] and board[x] != " ":
            return board[x]
    if " " not in board:
        return "Draw"
    return None

# computer move (not unbeatable, but plays decent)
def computer_move(board, comp, player):
    # try to win
    for i in range(9):
        if board[i] == " ":
            board[i] = comp
            if check_winner(board) == comp:
                board[i] = " "  # reset before confirming
                return i
            board[i] = " "
    # try to block
    for i in range(9):
        if board[i] == " ":
            board[i] = player
            if check_winner(board) == player:
                board[i] = " "
                return i
            board[i] = " "
    # else pick center if free
    if board[4] == " ":
        return 4
    # else random move
    free = [i for i in range(9) if board[i] == " "]
    return random.choice(free)

# main game loop
def play_game(vs_computer=False):
    board = [" "] * 9
    turn = "X"
    player = "X"
    comp = "O"

    while True:
        draw_board(board)

        if vs_computer and turn == comp:
            print("Computer is thinking...")
            time.sleep(1)
            move = computer_move(board, comp, player)
            print("Computer chose", move+1)
        else:
            try:
                move = int(input(f"Player {turn}, enter position (1-9): ")) - 1
            except ValueError:
                print("Please enter a number.")
                continue
            if move < 0 or move > 8 or board[move] != " ":
                print("Invalid move, try again.")
                continue

        board[move] = turn
        winner = check_winner(board)
        if winner:
            draw_board(board)
            if winner == "Draw":
                print("It's a draw!")
            else:
                print(f"{winner} wins the game!")
            break

        # swap turns
        turn = "O" if turn == "X" else "X"

# entry point
print("Welcome to Tic Tac Toe!")
print("1) Two players")
print("2) Play against computer")
choice = input("Choose mode (1/2): ")
if choice == "1":
    play_game(False)
else:
    play_game(True)
