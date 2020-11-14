def print_board(board):
    print("---------")
    print("| {} {} {} |".format(board[0], board[1], board[2]))
    print("| {} {} {} |".format(board[3], board[4], board[5]))
    print("| {} {} {} |".format(board[6], board[7], board[8]))
    print("---------")


def wins(board, symbol):
    if board[4] == symbol:
        if board[3] == symbol and board[5] == symbol:
            return True
        if board[2] == symbol and board[6] == symbol:
            return True
        if board[1] == symbol and board[7] == symbol:
            return True
        if board[0] == symbol and board[8] == symbol:
            return True
    elif board[0] == symbol:
        if board[1] == symbol and board[2] == symbol:
            return True
        if board[3] == symbol and board[6] == symbol:
            return True
    elif board[8] == symbol:
        if board[2] == symbol and board[5] == symbol:
            return True
        if board[6] == symbol and board[7] == symbol:
            return True
    else:
        return False


def game_state(board):
    if abs(board.count("X") - board.count("O")) > 1:
        print("Impossible")
    elif wins(board, "X"):
        if wins(board, "O"):
            print("Impossible")
        else:
            print("X wins")
    elif wins(board, "O"):
        print("O wins")
    elif "_" in board:
        print("Game not finished")
    else:
        print("Draw")


board = list(input("Enter cells: "))
print_board(board)
while True:
    coordinates = input("Enter the coordinates: ").split()
    if coordinates[0].isdigit() and coordinates[1].isdigit():
        coordinates = [int(x) for x in coordinates]
        if coordinates[0] in range(1, 4) and coordinates[1] in range(1, 4):
            address = coordinates[0] + 8 - 3 * coordinates[1]
            if board[address] != "_":
                print("This cell is occupied! Choose another one!")
                continue
            board[address] = "X"
            print_board(board)
            # game_state(board)
            break
        else:
            print("Coordinates should be from 1 to 3!")
    else:
        print("You should enter numbers!")