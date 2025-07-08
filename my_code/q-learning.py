# # from collections import defaultdict
# #
# # # Empty board
# # empty_board = (('-', '-', '-'),
# #                ('-', '-', '-'),
# #                ('-', '-', '-'))
# #
# # # Convert to tuple of tuples to make it hashable (i.e., usable as a dict key)
# # q_table = defaultdict(lambda: defaultdict(float))
# #
# # # Fill it with some fake Q-values (actions are (row, col))
# # q_table[empty_board][(0, 0)] = 0.5
# # q_table[empty_board][(0, 1)] = 0.2
# # q_table[empty_board][(1, 1)] = 0.8
# # q_table[empty_board][(2, 2)] = 0.3
# # def get_calculated_move(state, mark):
# #     selected_move = None
# #     best_q = float('-inf')
# #
# #     if state in q_table:
# #         print(state)
# #         for action, q in q_table[state].items():
# #             print(action)
# #             if q > best_q:
# #                 best_q = q
# #                 selected_move = action
# #
# #     return selected_move
# # state = empty_board
# # best_move = get_calculated_move(state, "X")
# # print("Best move:", best_move)
# board = [['-', '-', '-'],
#              ['-', '-', '-'],
#              ['-', '-', '-']]
#
# last_state = tuple(tuple(row) for row in board)
# print(last_state)
#
# state_after_key = get_tuple_state(state_after)
# # if state_after_key not in q_table:
# #     print("Adding unseen state:", state_after_key)
# #     for action in get_available_moves(state_after_key):
# #         q_table[state_after_key][action] = 0.0
# #     selected_move = get_random_move()
# #     print(f"Unseen state -> making random move: {selected_move}")
# reward = get_reward(state_after)
# if len(get_available_moves(state_after)) == 0:
#     new_estimate = reward
# else:
#     future_estimates = q_table[state_after_key]
#     # if not future_estimates:
#     #     new_estimate = reward
#     # else:
empty_board = (('-', '-', '-'),
               ('-', '-', '-'),
               ('-', '-', '-'))
for row in empty_board:
    print(row)
print(row)