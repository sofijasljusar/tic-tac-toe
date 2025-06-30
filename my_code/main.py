import random
from pprint import pprint
from collections import defaultdict

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

learning_rate = 0.3
discount_factor = 0.9
exploration_prob = 0.2
epochs = 3
q_table = defaultdict(lambda: defaultdict(float))


def is_victory(current_state):
    for state in winning_states:
        if (current_state[state[0][0]][state[0][1]]
                == current_state[state[1][0]][state[1][1]]
                == current_state[state[2][0]][state[2][1]] != '-'):
            print(f"{current_state[state[0][0]][state[0][1]]} won!")
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
            row = int(input("Select row (1-3): ")) - 1
            column = int(input("Select column (1-3): ")) - 1
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


def get_calculated_move(state, mark):
    dictionary_state = tuple(tuple(row) for row in state)
    if dictionary_state not in q_table:
        print("Need to add state to table!")
        print("...with what value?")
    best_q = float('-inf')
    selected_move = None
    for state in q_table:
        print(state)
        for action, q in q_table[state].items():
            print(action)
            if q > best_q:
                best_q = q
                selected_move = action
    print(f"Top Q-Value: {best_q}")
    print(f"Best move: {selected_move}")
    board[selected_move[0]][selected_move[1]] = mark

# for epoch in range(epochs):
#     board = [['-', '-', '-'],
#              ['-', '-', '-'],
#              ['-', '-', '-']]
#
#     print("The Game of Tic-Tac-Toe")
#     first_player = random.choice(players)
#
#
#     def game(player=first_player):
#         iteration = 0
#         while iteration < 9:
#             iteration += 1
#             print(f"Player {player} move...")
#             if player == "X":
#                 get_random_move(player)
#             else:
#                 get_human_move(player)
#
#             player = 'O' if player == 'X' else 'X'
#
#             for line in board:
#                 print(' '.join(line))
#             if is_victory(board):
#                 iteration = 10
#             if iteration == 9:
#                 print("It's a draw!")
#         print("Game over!")
#
#     game(first_player)


board = [['-', '-', '-'],
         ['O', 'X', '-'],
         ['O', '-', '-']]

tuple_board = tuple(tuple(row) for row in board)

q_table[tuple_board][(0, 0)] = 0.8
q_table[tuple_board][(0, 1)] = 0.5
q_table[tuple_board][(1, 2)] = 0.2
q_table[tuple_board][(2, 2)] = 0.6

get_calculated_move(board, "X")
print(board)
pprint(q_table)

