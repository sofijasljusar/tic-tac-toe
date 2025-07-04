import random
from pprint import pprint
from collections import defaultdict
from copy import deepcopy

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
epochs = 10
q_table = defaultdict(lambda: defaultdict(float))


def is_winner(current_state):
    for state in winning_states:
        if (current_state[state[0][0]][state[0][1]]
                == current_state[state[1][0]][state[1][1]]
                == current_state[state[2][0]][state[2][1]] != '-'):
            winner = current_state[state[0][0]][state[0][1]]
            print(f"{winner} won!")
            return winner
    return None


def move_is_valid(x, y):
    if x > 2 or x < 0 or y > 2 or y < 0:
        print("Please, enter a number between 1 and 3!")
        return False
    elif board[x][y] != '-':
        print("This position is taken!")
        return False
    else:
        return True


def get_human_move():
    valid_move_made = False
    while not valid_move_made:
        try:
            row = int(input("Select row (1-3): ")) - 1
            column = int(input("Select column (1-3): ")) - 1
            if move_is_valid(row, column):
                valid_move_made = True
        except ValueError:
            print("Please enter a valid number!")
    return (row, column)


def get_available_moves(current_state):
    positions = []
    for i in range(3):
        for j in range(3):
            if current_state[i][j] == '-':
                positions.append((i, j))
    return positions


def get_random_move():
    selected_move = random.choice(get_available_moves(board))
    return selected_move


def get_tuple_state(list_board):
    return tuple(tuple(row) for row in list_board)


def get_reward(state):
    if len(get_available_moves(state)) == 0:
        winner = is_winner(state)
        if winner:
            if winner == "X":
                return 1.0
            elif winner == "O":
                return -1.0
        else:
            return 0.5
    else:
        return 0.0


def get_next_state(state, action):
    next_state = deepcopy(state)
    next_state[action[0]][action[1]] = "X"
    return next_state


def update_q_value(state, action):
    current_state_key = get_tuple_state(state)
    state_after = get_next_state(state, action)
    state_after_key = get_tuple_state(state_after)
    reward = get_reward(state_after)
    if len(get_available_moves(state_after)) == 0:
        new_estimate = reward
    else:
        future_estimates = q_table[state_after_key]
        new_estimate = reward + (discount_factor * max(future_estimates.values()))
    change = learning_rate * (new_estimate - q_table[current_state_key][action])
    q_table[current_state_key][action] += change
    print(f"Updating Q[{current_state_key}][{action}] with new estimate {q_table[current_state_key][action]}")


def get_calculated_move(state):
    selected_move = None
    available_moves = get_available_moves(state)
    dictionary_state = get_tuple_state(state)
    if dictionary_state not in q_table:
        print("Adding unseen state:", dictionary_state)
        for action in available_moves:
            q_table[dictionary_state][action] = 0.0
        selected_move = get_random_move()
        print(f"Unseen state -> making random move: {selected_move}")
    else:
        if all(q == 0.0 for q in q_table[dictionary_state].values()):
            selected_move = get_random_move()
            print(f"All values 0s -> making random move: {selected_move}")
        else:
            if random.random() < exploration_prob:
                selected_move = get_random_move()
                print(f"Exploration rate -> exploring new move: {selected_move}")
            else:
                best_q = float('-inf')
                for action, q in q_table[dictionary_state].items():
                    print(action)
                    if q > best_q:
                        best_q = q
                        selected_move = action
                print(f"Top Q-Value: {best_q}")
                print(f"Best move: {selected_move}")
    return selected_move


for epoch in range(epochs):
    board = [['-', '-', '-'],
             ['-', '-', '-'],
             ['-', '-', '-']]

    print("The Game of Tic-Tac-Toe")
    first_player = random.choice(players)

    def game(player=first_player):
        iteration = 0
        while iteration < 9:
            iteration += 1
            print(f"Player {player} move...")
            if player == "X":
                move = get_calculated_move(board)
                update_q_value(board, move)
                board[move[0]][move[1]] = player
            else:
                move = get_human_move()
                board[move[0]][move[1]] = player

            player = 'O' if player == 'X' else 'X'

            for line in board:
                print(' '.join(line))
            if is_winner(board):
                iteration = 10
            if iteration == 9:
                print("It's a draw!")
        print("Game over!")
        pprint(q_table)

    game(first_player)

pprint(q_table)

