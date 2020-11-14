from random import randint

rep_board1 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]


def randX(a, b, c, row):
    try:
        x = randint(a, len(rep_board1[row])-b)

        if rep_board1[row][x] != 0:
            return x

        if x == 1:
            x += c

        for col in range(len(rep_board1[row])):
            if rep_board1[0][col] == 0 and rep_board1[1][col] == 0 and rep_board1[2][col] == 0:
                if col == 0:
                    return randX(a+1, b, c, row)

                elif col == 2:
                    return randX(a, b+1, c, row)

                elif col == 1:
                    return randX(a, b, c+1, row)

        if (rep_board1[0][1] == 0 and rep_board1[1][1] == 0 and rep_board1[2][1] == 0) and (rep_board1[2] == 0 and rep_board1[1][2] == 0 and rep_board1[2][2] == 0):
            return randX(a, b, c-2, row)

    except:
        for x in range(len(rep_board1[1])):
            if rep_board1[1][x] != 0:
                return x


def positi(a, b, c):
    y = randint(a, len(rep_board1)-b)

    if rep_board1[y] != 0:
        x = randX(0, 1, 0, y)
        if x is None:
            x = 0
        return y, x

    if y == 1:
        y += c

    for row in range(len(rep_board1)):
        if rep_board1[row][0] == 0 and rep_board1[row][1] == 0 and rep_board1[row][2] == 0:
            if row == 0:
                return positi(a+1, b, c)

            elif row == 2:
                return positi(a, b+1, c)

            elif row == 1:
                return positi(a, b, c+1)

    if (rep_board1[1][0] == 0 and rep_board1[1][1] == 0 and rep_board1[1][2] == 0) and (rep_board1[2][0] == 0 and rep_board1[2][1] == 0 and rep_board1[2][2] == 0):
        return positi(a, b, c-2)
