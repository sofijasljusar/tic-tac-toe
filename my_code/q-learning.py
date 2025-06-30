# from collections import defaultdict
#
# # Empty board
# empty_board = (('-', '-', '-'),
#                ('-', '-', '-'),
#                ('-', '-', '-'))
#
# # Convert to tuple of tuples to make it hashable (i.e., usable as a dict key)
# q_table = defaultdict(lambda: defaultdict(float))
#
# # Fill it with some fake Q-values (actions are (row, col))
# q_table[empty_board][(0, 0)] = 0.5
# q_table[empty_board][(0, 1)] = 0.2
# q_table[empty_board][(1, 1)] = 0.8
# q_table[empty_board][(2, 2)] = 0.3
# def get_calculated_move(state, mark):
#     selected_move = None
#     best_q = float('-inf')
#
#     if state in q_table:
#         print(state)
#         for action, q in q_table[state].items():
#             print(action)
#             if q > best_q:
#                 best_q = q
#                 selected_move = action
#
#     return selected_move
# state = empty_board
# best_move = get_calculated_move(state, "X")
# print("Best move:", best_move)
board = [['-', '-', '-'],
             ['-', '-', '-'],
             ['-', '-', '-']]

last_state = tuple(tuple(row) for row in board)
print(last_state)