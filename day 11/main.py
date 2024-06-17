# project Permainan TIC-TAC-TOE menggunakan bahasa pemerograman python
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)
        
def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        row = int(input(f"{player}'s turn. Enter row (1-3): "))
        col = int(input(f"{player}'s turn. Enter column (1-3): "))
        if board[row - 1][col - 1] == " ":
            board[row - 1][col - 1] = player
            if check_winner(board, player):
                print_board(board)
                print(f"{player} wins!")
                break
            if check_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken. Try again.")

tic_tac_toe()