import math
from .minimax import rep_board, get_winner

count = 0


def minimaxMed(depth, isMaximizer, board=rep_board):

    global count
    count += 1
    winner = get_winner(board)

    if depth == 0:
        return (1, 0, 0)

    if winner == 'X':
        return (-1, 0, 0)

    elif winner == 'O':
        return (1, 0, 0)

    elif winner == '.':
        return (0, 0, 0)

    if isMaximizer:
        maxEval = -math.inf
        bestIdex = (None, None)

        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] == '.':
                    board[i][j] = 'O'
                    (eval, min_i, min_j) = minimaxMed(depth - 1, False, board)
                    if eval > maxEval:
                        maxEval = eval
                        bestIdex = (i, j)
                    board[i][j] = '.'
        return (maxEval, bestIdex[0], bestIdex[1])

    else:
        minEval = math.inf
        worstIndex = (None, None)

        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] == '.':
                    board[i][j] = 'X'
                    (eval, max_i, max_j) = minimaxMed(depth - 1, board)
                    if eval < minEval:
                        minEval = eval
                        worstIndex = (i, j)
                    board[i][j] = '.'
        return (minEval, worstIndex[0], worstIndex[1])
