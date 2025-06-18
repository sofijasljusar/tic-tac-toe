
winning_states = [
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)]
]


board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]


def is_victory(current_state):
    for state in winning_states:
        if ('X' == current_state[state[0][0]][state[0][1]]
                == current_state[state[1][0]][state[1][1]]
                == current_state[state[2][0]][state[2][1]]):
            print("X won!")
            return True
        elif ('0' == current_state[state[0][0]][state[0][1]]
                  == current_state[state[1][0]][state[1][1]]
                  == current_state[state[2][0]][state[2][1]]):
            print("0 won!")
            return True
    return False


# def game_continues(current_state):
#     for current_row in current_state:
#         for position in current_row:
#             if position == '-':
#                 return False
#     return False


def move_is_valid(x, y):
    if x > 2 or x < 0 or y > 2 or y < 0:
        print("Please, enter a number between 1 and 3!")
        return False
    elif board[x][y] != '-':
        print("This position is taken!")
        return False
    else:
        return True


def make_move(mark):
    valid_move_made = False
    while not valid_move_made:
        try:
            row = int(input("Select row (1-3): "))-1
            column = int(input("Select column (1-3): "))-1
            if move_is_valid(row, column):
                board[row][column] = mark
                valid_move_made = True
        except ValueError:
            print("Please enter a valid number!")


iteration = 0

while iteration < 9:
    iteration += 1
    player = 'X' if iteration % 2 == 1 else '0'
    print(f"Player {player} move...")
    make_move(player)
    for line in board:
        print(' '.join(line))
    if is_victory(board):
        iteration = 10
    if iteration == 9:
        print("It's a draw!")
print("Game over!")
