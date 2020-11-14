import math

count = 0
rep_board = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]


def get_winner(board):
    for i in range(0, 3):
        if (board[0][i] != '.' and
            board[0][i] == board[1][i] and
                board[1][i] == board[2][i]):
            return board[0][i]

    for i in range(0, 3):
        if (board[i] == ['X', 'X', 'X']):
            return 'X'
        elif (board[i] == ['O', 'O', 'O']):
            return 'O'

    if (board[0][0] != '.' and
        board[0][0] == board[1][1] and
            board[0][0] == board[2][2]):
        return board[0][0]

    if (board[0][2] != '.' and
        board[0][2] == board[1][1] and
            board[0][2] == board[2][0]):
        return board[0][2]

    for i in range(0, 3):
        for j in range(0, 3):
            if (board[i][j] == '.'):
                return None

    return '.'


def minimaxAB(depth, alpha, beta, isMaximizer, board=rep_board):

    winner = get_winner(board)

    if winner == 'X':
        return (-10 + depth, 0, 0)

    elif winner == 'O':
        return (10 - depth, 0, 0)

    elif winner == '.':
        return (0, 0, 0)

    if isMaximizer:
        maxEval = -math.inf
        bestIndex = (None, None)
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] == '.':
                    board[i][j] = 'O'
                    (eval, min_i, min_j) = minimaxAB(
                        depth + 1, alpha, beta, False, board)
                    if eval > maxEval:
                        maxEval = eval
                        bestIndex = (i, j)
                    board[i][j] = '.'

                    if maxEval >= beta:
                        return (maxEval, bestIndex[0], bestIndex[1])

                    if maxEval > alpha:
                        alpha = maxEval

        return (maxEval, bestIndex[0], bestIndex[1])

    else:
        minEval = math.inf
        worstIndex = (None, None)
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] == '.':
                    board[i][j] = 'X'
                    (eval, max_i, max_j) = minimaxAB(
                        depth + 1, alpha, beta, True, board)
                    if eval < minEval:
                        minEval = eval
                        worstIndex = (i, j)
                    board[i][j] = '.'

                    if minEval <= alpha:
                        return (minEval, worstIndex[0], worstIndex[1])

                    if minEval < beta:
                        beta = minEval

        return (minEval, worstIndex[0], worstIndex[1])


""" def minimax(depth, isMaximizer, board=rep_board):

    global count
    winner = get_winner(board)
    count += 1

    if winner == 'X':
        return (-10 + depth, 0, 0)

    elif winner == 'O':
        return (10 - depth, 0, 0)

    elif winner == '.':
        return (0, 0, 0)

    if isMaximizer:
        maxEval = -math.inf
        bestIndex = (None, None)
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] == '.':
                    board[i][j] = 'O'
                    (eval, min_i, min_j) = minimax(depth + 1, False, board)
                    if eval > maxEval:
                        maxEval = eval
                        bestIndex = (i, j)
                    board[i][j] = '.'
        return (maxEval, bestIndex[0], bestIndex[1])

    else:
        minEval = math.inf
        worstIndex = (None, None)
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] == '.':
                    board[i][j] = 'X'
                    (eval, max_i, max_j) = minimax(depth + 1, True, board)
                    if eval < minEval:
                        minEval = eval
                        worstIndex = (i, j)
                    board[i][j] = '.'
        return (minEval, worstIndex[0], worstIndex[1]) """
