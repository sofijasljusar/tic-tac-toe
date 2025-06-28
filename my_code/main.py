import random

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
players = ["X", "O"]


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
        elif ('O' == current_state[state[0][0]][state[0][1]]
                  == current_state[state[1][0]][state[1][1]]
                  == current_state[state[2][0]][state[2][1]]):
            print("O won!")
            return True
    return False


def move_is_valid(x, y):
    if x > 2 or x < 0 or y > 2 or y < 0:
        print("Please, enter a number between 1 and 3!")
        return False
    elif board[x][y] != '-':
        print("This position is taken!")
        return False
    else:
        return True


def get_human_move(mark):
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


def get_available_moves(current_state):
    positions = []
    for i in range(3):
        for j in range(3):
            if current_state[i][j] == '-':
                positions.append((i, j))
    return positions


def get_random_move(mark):
    selected_move = random.choice(get_available_moves(board))
    board[selected_move[0]][selected_move[1]] = mark


print("The Game of Tic-Tac-Toe")
player = random.choice(players)

iteration = 0
while iteration < 9:
    iteration += 1
    print(f"Player {player} move...")
    if player == "X":
        get_random_move(player)
    else:
        get_human_move(player)

    player = 'O' if player == 'X' else 'X'

    for line in board:
        print(' '.join(line))
    if is_victory(board):
        iteration = 10
    if iteration == 9:
        print("It's a draw!")
print("Game over!")
