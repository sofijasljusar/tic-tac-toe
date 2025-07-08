"""
I did it badly, but I did it!
This is a play against random opponent and the agent is learning from immediate rewards.
The stats are: (tested for small nuber of games for now to see all the nuances)
At 50 games, the current stats are:
Wins: 22
Losses: 23
Stalemate: 5
Current epsilon value: 0.2
Win rate is 44.0%

And in q-table, we can see that the agent learns winning moves and remembers how not to do:
(('X', 'X', '-'), ('O', '-', 'O'), ('-', '-', '-')): defaultdict(<class 'float'>,
                                                                              {(0, 2): 0.29895,
                                                                               (1, 1): 0.0,
                                                                               (2, 0): 0.0,
                                                                               (2, 1): 0.0,
                                                                               (2, 2): 0.0})
(('O', 'X', 'X'), ('X', '-', 'O'), ('O', '-', 'O')): defaultdict(<class 'float'>,
                                                                              {(1, 1): 0.0,
                                                                               (2, 1): -0.30105})

> > > Testing with more epochs > > >
At 100 games, the current stats are:
Wins: 47
Losses: 43
Stalemate: 10
Current epsilon value: 0.2
Win rate is 47.0%

=========== Training Results ===========
At 500 games, the current stats are:
Wins: 244
Losses: 209
Stalemate: 47
Current epsilon value: 0.2
Win rate is 48.8%

=========== Training Results ===========
At 1000 games, the current stats are:
Wins: 471
Losses: 404
Stalemate: 125
Current epsilon value: 0.2
Win rate is 47.099999999999994%

=========== Training Results ===========
At 10000 games, the current stats are:
Wins: 5765
Losses: 2945
Stalemate: 1290
Current epsilon value: 0.2
Win rate is 57.65%

=========== Training Results ===========
At 20000 games, the current stats are:
Wins: 12589
Losses: 4724
Stalemate: 2687
Current epsilon value: 0.2
Win rate is 62.94499999999999%

=========== Training Results ===========
At 50000 games, the current stats are:
Wins: 34419
Losses: 8438
Stalemate: 7143
Current epsilon value: 0.2
Win rate is 68.838%

=========== Training Results ===========
At 100000 games, the current stats are:
Wins: 71564
Losses: 14674
Stalemate: 13762
Current epsilon value: 0.2
Win rate is 71.56400000000001%

=========== Training Results ===========
At 200000 games, the current stats are:
Wins: 145848
Losses: 26869
Stalemate: 27283
Current epsilon value: 0.2
Win rate is 72.924%
"""

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
epochs = 200000
q_table = defaultdict(lambda: defaultdict(float))

wins = 0
loses = 0
stalemate = 0
# total_games = 0


def is_winner(current_state):
    for state in winning_states:
        if (current_state[state[0][0]][state[0][1]]
                == current_state[state[1][0]][state[1][1]]
                == current_state[state[2][0]][state[2][1]] != '-'):
            winner = current_state[state[0][0]][state[0][1]]
            # print(f"{winner} won!")
            return winner
    return None


def is_terminal(state):
    return is_winner(state) is not None or len(get_available_moves(state)) == 0


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
    winner = is_winner(state)
    if winner:
        if winner == "X":
            return 1.0
        elif winner == "O":
            return -1.0
    elif len(get_available_moves(state)) == 0:
        return 0.5
    else:
        return 0.0


def get_next_state(state, action):
    next_state = deepcopy(state)
    next_state[action[0]][action[1]] = "X"
    return next_state


def update_q_value(state, action, reward):
    current_state_key = get_tuple_state(state)
    # state_after = get_next_state(state, action)
    # state_after_key = get_tuple_state(state_after)
    # if is_terminal(state_after):
    #     new_estimate = reward
    # else:
    #     future_estimates = q_table[state_after_key]
    #     new_estimate = reward + (discount_factor * max(future_estimates.values()))
    change = learning_rate * (reward - q_table[current_state_key][action])
    q_table[current_state_key][action] += change
    # print(f"Updating Q[{current_state_key}][{action}] with new estimate {q_table[current_state_key][action]}")


def get_calculated_move(state):
    selected_move = None
    available_moves = get_available_moves(state)
    dictionary_state = get_tuple_state(state)
    if dictionary_state not in q_table:
        # print("Adding unseen state:", dictionary_state)
        for action in available_moves:
            q_table[dictionary_state][action] = 0.0
        selected_move = get_random_move()
        # print(f"Unseen state -> making random move: {selected_move}")
    else:
        if all(q == 0.0 for q in q_table[dictionary_state].values()):
            selected_move = get_random_move()
            # print(f"All values 0s -> making random move: {selected_move}")
        else:
            if random.random() < exploration_prob:
                selected_move = get_random_move()
                # print(f"Exploration rate -> exploring new move: {selected_move}")
            else:
                best_q = float('-inf')
                for action, q in q_table[dictionary_state].items():
                    # print(action)
                    if q > best_q:
                        best_q = q
                        selected_move = action
                # print(f"Top Q-Value: {best_q}")
                # print(f"Best move: {selected_move}")
    return selected_move

def game(player):
    global wins, loses, stalemate, total_games
    iteration = 0
    while iteration < 9:
        iteration += 1
        # print(f"Player {player} move...")
        if player == "X":
            agent_move = get_calculated_move(board)
            update_q_value(board, agent_move, -0.005)
            previous_state = deepcopy(board)
            board[agent_move[0]][agent_move[1]] = player
        else:
            random_move = get_random_move()
            board[random_move[0]][random_move[1]] = player

        player = 'O' if player == 'X' else 'X'

        # for line in board:
            # print(' '.join(line))
        winner = is_winner(board)
        if winner:
            iteration = 10
            reward = get_reward(board)
            update_q_value(previous_state, agent_move, reward)
            if winner == "X":
                wins += 1
            else:
                loses += 1
        if iteration == 9:
            stalemate += 1
            # print("It's a draw!")
            reward = get_reward(board)
            update_q_value(previous_state, agent_move, reward)
    # print("Game over!")

for epoch in range(epochs):
    board = [['-', '-', '-'],
             ['-', '-', '-'],
             ['-', '-', '-']]

    # print("The Game of Tic-Tac-Toe")
    first_player = random.choice(players)
    game(first_player)

print("=========== Training Results ===========")
print(f"At {epochs} games, the current stats are:")
print(f"Wins: {wins}")
print(f"Losses: {loses}")
print(f"Stalemate: {stalemate}")
print(f"Current epsilon value: {exploration_prob}")
print(f"Win rate is {(wins/epochs) * 100}%")
# pprint(q_table)

# TODO: How would it be handled? if values are ==, then choose at random;
#  I think it should find the min value, then compare all to max, if couple -> choose at random
#  {(('-', '-', '-'), ('-', '-', '-'), ('-', '-', '-')): defaultdict(<class 'float'>,
#                                                                               {(0, 0): -0.0045882284999999995,
#                                                                                (0, 1): -0.004411755,
#                                                                                (0, 2): -0.0045882284999999995,
#                                                                                (1, 0): -0.0045882284999999995,
#                                                                                (1, 1): -0.004411755,
#                                                                                (1, 2): -0.004411755,
#                                                                                (2, 0): -0.004411755,
#                                                                                (2, 1): -0.004411755,
#                                                                                (2, 2): -0.004411755}),
#