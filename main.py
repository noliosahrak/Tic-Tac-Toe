def print_board(field):
    print("---------")
    print("| {} {} {} |".format(field[0], field[1], field[2]))
    print("| {} {} {} |".format(field[3], field[4], field[5]))
    print("| {} {} {} |".format(field[6], field[7], field[8]))
    print("---------")


def wins(field, symbol):
    if field[4] == symbol:
        if field[3] == symbol and field[5] == symbol:
            return True
        if field[2] == symbol and field[6] == symbol:
            return True
        if field[1] == symbol and field[7] == symbol:
            return True
        if field[0] == symbol and field[8] == symbol:
            return True
    elif field[0] == symbol:
        if field[1] == symbol and field[2] == symbol:
            return True
        if field[3] == symbol and field[6] == symbol:
            return True
    elif field[8] == symbol:
        if field[2] == symbol and field[5] == symbol:
            return True
        if field[6] == symbol and field[7] == symbol:
            return True
    else:
        return False


def game_state(field):
    if wins(field, "X"):
        return "X wins"
    elif wins(field, "O"):
        return "O wins"
    elif "_" in field:
        return "Game not finished"
    else:
        return "Draw"


def move(symbol):
    while True:
        coordinates = input("Enter the coordinates: ").split()
        if coordinates[0].isdigit() and coordinates[1].isdigit():
            coordinates = [int(x) for x in coordinates]
            if coordinates[0] in range(1, 4) and coordinates[1] in range(1, 4):
                address = coordinates[0] + 8 - 3 * coordinates[1]
                global board
                if board[address] != "_":
                    print("This cell is occupied! Choose another one!")
                    continue
                board[address] = symbol
                print_board(board)
                break
            else:
                print("Coordinates should be from 1 to 3!")
        else:
            print("You should enter numbers!")


board = "_ _ _ _ _ _ _ _ _".split()
print_board(board)
turn_X = True
while game_state(board) == "Game not finished":
    if turn_X:
        move("X")
    else:
        move("O")
    turn_X = not turn_X
print(game_state(board))
