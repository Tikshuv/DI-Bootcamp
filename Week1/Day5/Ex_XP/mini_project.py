def create_board():
    # board 15 * 7
    columns = 15
    rows = 7
    board = [[] for i in range(7)]
    for r in range(rows):
        for c in range(columns):
            board[r].append('')
    for r in range(rows):
        for c in range(columns):
            if (r == 0 or c == 0) or (r == rows - 1 or c == columns - 1):  # filling sides with *
                board[r][c] = '*'
            else:
                board[r][c] = ' '
            if (r == 2 or r == 4) and (1 < c < columns - 2):  # creating rows for the board
                board[r][c] = '-'

            if (0 < r < rows - 1) and (c == 5 or c == 9):  # creating columns for the board
                board[r][c] = '|'

    for row in board:
        print(''.join(row))
    return board


def display_board(board):
    for row in board:
        print(''.join(row))


def player_input(position):
    while True:
        position = input(f"Select a {position}(between 1 and 3: ")
        position = ''.join(num for num in position if num.isdigit())

        if not position.isdigit():
            continue
        position = int(position)

        if not 0 < position < 4:  # check for valid input of a column
            print("Please, type only a number between 1 and 3\n")
            continue
        break
    return position


def check_win(board, rows, columns):
    values = []
    win_condition = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)]
    ]
    for cond in win_condition:
        for x, y in cond:
            values.append(board[rows[x]][columns[y]])
            # values = [board[rows[x]][[columns[y]]] for x, y in cond]
        if values[0] != ' ' and values.count(values[0]) == 3:
            print(f"And the winner is: {values[0]}")
            return values[0]
        values = []


def player_turn(player, board, rows, columns):
    while True:
        print(f"It's {player}'s turn")
        row = rows[player_input('row')-1]
        column = columns[player_input('column')-1]
        if board[row][column] == ' ':
            board[row][column] = player
            break
        print("Occupied cell, choose another\n")


def play():
    game = create_board()
    playable_cells = {'rows': [1, 3, 5], 'columns': [3, 7, 11]}  # storing cells that'll be used for the game
    player_r = 0
    player_c = 0
    players = ['', 'X', '0']
    c_player = 1
    check = 0
    flag = 0

    while not check:
        player_turn(players[c_player], game, playable_cells['rows'], playable_cells['columns'])
        display_board(game)
        check = check_win(game, playable_cells['rows'], playable_cells['columns'])
        flag += 1
        if flag == 9:
            print("That's a DRAW")
            break
        c_player *= -1


play()
