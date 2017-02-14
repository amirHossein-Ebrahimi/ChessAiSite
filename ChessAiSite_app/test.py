statebeeease = [
    ["0", "-a", "-b", "-c", "-d", "-e", "-f", "-g", "-h"],
    ["8", "R", "K", "B", "Q", "S", "B", "K", "R"],
    ["7", "P", "P", "P", "P", "P", "P", "P", "P"],
    ["6", ".", ".", ".", ".", ".", ".", ".", "."],
    ["5", ".", ".", ".", ".", ".", ".", ".", "."],
    ["4", ".", ".", ".", ".", ".", ".", ".", "."],
    ["3", ".", ".", ".", ".", ".", ".", ".", "."],
    ["2", "p", "p", "p", "p", ".", "p", "p", "p"],
    ["1", "r", "k", "b", "q", "s", "b", "k", "r"]
]

statebase = [
    ["0", "1", "2", "3", "4", "5", "6", "7", "8"],
    ["1", "R", "K", "B", "Q", "S", "B", "K", "R"],
    ["2", "P", "P", "P", "P", "P", "P", "P", "P"],
    ["3", ".", ".", ".", ".", ".", ".", ".", "."],
    ["4", ".", ".", ".", ".", ".", ".", ".", "."],
    ["5", ".", ".", ".", ".", ".", ".", ".", "."],
    ["6", ".", ".", ".", ".", ".", ".", ".", "."],
    ["7", "p", "p", "p", "p", "p", "p", "p", "p"],
    ["8", "r", "k", "b", "q", "s", "b", "k", "r"]
]
(7, 5, 6, 1)


def enemy_analisor(color, n):
    if color == "w":
        if 'A' <= n <= 'Z':
            return True
    elif color == "b":
        if 'a' <= n <= 'z':
            return True
    else:
        return False


def empty_analisor(n):
    if n == ".":
        return True
    else:
        return False


def out_of_range(i, j):
    if i > 8 or j > 8 or i < 1 or j < 1:
        return True
    else:
        return False


def friend_analisor(color, n):
    if color == "w":
        if 'a' <= n <= 'z':
            return True
    elif color == "b":
        if 'A' <= n <= 'Z':
            return True
    else:
        return False


def pices_caller(state, i, j, color, function_name):
    return function_name(state, i, j, color)


def Pawn(state, i, j, color):
    possible_moves = []
    if color == "w":
        if i == 7:
            if empty_analisor(state[i - 1][j]):
                possible_moves.append((i - 1, j))

            if empty_analisor(state[i - 1][j]) and empty_analisor([state[i - 2][j]]):
                possible_moves.append((i - 2, j))
                if not out_of_range(i - 1, j - 1):
                    if enemy_analisor(color, state[i - 1][j - 1]):
                        possible_moves.append((i - 1, j - 1))
                if not out_of_range(i - 1, j + 1):
                    if enemy_analisor(color, state[i - 1][j + 1]):
                        possible_moves.append((i - 1, j + 1))
            if i != 7:
                if not out_of_range(i - 1, j):
                    if empty_analisor(state[i - 1][j]):
                        possible_moves.append((i - 1, j))
                if not out_of_range(i - 1, j - 1):
                    if enemy_analisor(color, state[i - 1][j - 1]):
                        possible_moves.append((i - 1, j - 1))
                if not out_of_range(i - 1, j + 1):
                    if enemy_analisor(color, state[i - 1][j + 1]):
                        possible_moves.append((i - 1, j + 1))

    if color == "b":
        if i == 2:
            if empty_analisor(state[i + 1][j]):
                possible_moves.append((i + 1, j))

        if empty_analisor(state[i + 1][j]) and empty_analisor[state[i + 2][j]]:
            possible_moves.append((i + 2, j))
            if not out_of_range(i + 1, j - 1):
                if enemy_analisor(color, state[i + 1][j - 1]):
                    possible_moves.append((i + 1, j - 1))
            if not out_of_range(i + 1, j + 1):
                if enemy_analisor(color, state[i + 1][j + 1]):
                    possible_moves.append((i + 1, j + 1))
        if i != 2:
            if not out_of_range(i + 1, j):
                if empty_analisor(state[i + 1][j]):
                    possible_moves.append((i + 1, j))
            if not out_of_range(i + 1, j - 1):
                if enemy_analisor(color, state[i + 1][j - 1]):
                    possible_moves.append((i + 1, j - 1))
            if not out_of_range(i + 1, j + 1):
                if enemy_analisor(color, state[i + 1][j + 1]):
                    possible_moves.append((i + 1, j + 1))
    return possible_moves


def Pawn(state, i, j, color):
    possible_moves = []
    if color == "w":
        if i == 7:
            if empty_analisor(state[i - 1][j]):
                possible_moves.append((i - 1, j))
            if empty_analisor(state[i - 1][j]) and empty_analisor(state[i - 2][j]):
                possible_moves.append((i - 2, j))
            if not out_of_range(i - 1, j - 1):
                if enemy_analisor(color, state[i - 1][j - 1]):
                    possible_moves.append((i - 1, j - 1))
            if not out_of_range(i - 1, j + 1):
                if enemy_analisor(color, state[i - 1][j + 1]):
                    possible_moves.append((i - 1, j + 1))
        else:
            if not out_of_range(i - 1, j):
                if empty_analisor(state[i - 1][j]):
                    possible_moves.append((i - 1, j))
            if not out_of_range(i - 1, j - 1):
                if enemy_analisor(color, state[i - 1][j - 1]):
                    possible_moves.append((i - 1, j - 1))
            if not out_of_range(i - 1, j + 1):
                if enemy_analisor(color, state[i - 1][j + 1]):
                    possible_moves.append((i - 1, j + 1))

    if color == "b":
        if i == 2:
            if empty_analisor(state[i + 1][j]):
                possible_moves.append((i + 1, j))
            if empty_analisor(state[i + 1][j]) and empty_analisor(state[i + 2][j]):
                possible_moves.append((i + 2, j))
            if not out_of_range(i + 1, j - 1):
                if enemy_analisor(color, state[i + 1][j - 1]):
                    possible_moves.append((i + 1, j - 1))
            if not out_of_range(i + 1, j + 1):
                if enemy_analisor(color, state[i + 1][j + 1]):
                    possible_moves.append((i + 1, j + 1))
        else:
            if not out_of_range(i + 1, j):
                if empty_analisor(state[i + 1][j]):
                    possible_moves.append((i + 1, j))
            if not out_of_range(i + 1, j - 1):
                if enemy_analisor(color, state[i + 1][j - 1]):
                    possible_moves.append((i + 1, j - 1))
            if not out_of_range(i + 1, j + 1):
                if enemy_analisor(color, state[i + 1][j + 1]):
                    possible_moves.append((i + 1, j + 1))
    return possible_moves


def Rook(state, i, j, color):
    possible_moves = []
    row_index, column_index = i, j
    for i in range(row_index + 1, 9):
        if empty_analisor(state[i][column_index]):
            possible_moves.append((i, column_index))
        if enemy_analisor(color, state[i][column_index]):
            possible_moves.append((i, column_index))
            break
        if friend_analisor(color, state[i][column_index]): break

    for i in range(row_index - 1, 0, -1):
        if empty_analisor(state[i][column_index]):
            possible_moves.append((i, column_index))
        if enemy_analisor(color, state[i][column_index]):
            possible_moves.append((i, column_index))
            break
        if friend_analisor(color, state[i][column_index]):
            break

    for j in range(column_index + 1, 9):
        if empty_analisor(state[row_index][j]): possible_moves.append((row_index, j))
        if enemy_analisor(color, state[row_index][j]):
            possible_moves.append((row_index, j))
            break
        if friend_analisor(color, state[row_index][j]):
            break

    for j in range(column_index - 1, 0, -1):
        if empty_analisor(state[row_index][j]): possible_moves.append((row_index, j))
        if enemy_analisor(color, state[row_index][j]):
            possible_moves.append((row_index, j))
            break
        if friend_analisor(color, state[row_index][j]):
            break

    return possible_moves


def Bishop(state, i, j, color):
    possible_moves = []
    direction = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
    row_index, column_index = i, j
    ai, aj = i, j
    for dirs in direction:
        ai, aj = i, j
        ai += dirs[0]
        aj += dirs[1]
        while (not out_of_range(ai, aj)):
            if friend_analisor(color, state[ai][aj]): break
            if empty_analisor(state[ai][aj]):
                possible_moves.append((ai, aj))
            if enemy_analisor(color, state[ai][aj]):
                possible_moves.append((ai, aj))
                break
            ai += dirs[0]
            aj += dirs[1]
    return possible_moves


def Queen(state, i, j, color):
    possible_moves = []
    for element in Rook(state, i, j, color):
        possible_moves.append(element)
    for element in Bishop(state, i, j, color):
        possible_moves.append(element)
    return possible_moves


def Knight(state, i, j, color):
    possible_moves = []
    elementry_moves = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
    # alternative i and j
    ai, aj = i, j
    for moves in elementry_moves:
        ai, aj = i, j
        ai += moves[0]
        aj += moves[1]
        if (not out_of_range(ai, aj)):
            if empty_analisor(state[ai][aj]): possible_moves.append((ai, aj))
            if enemy_analisor(color, state[ai][aj]):
                possible_moves.append((ai, aj))
    return possible_moves


def King(state, i, j, color):
    possible_moves = []
    elementry_moves = [(1, 1), (1, -1), (-1, -1), (-1, 1), (1, 0), (0, 1), (0, -1), (-1, 0)]
    ai, aj = i, j
    for moves in elementry_moves:
        ai, aj = i, j
        ai += moves[0]
        aj += moves[1]
        if (not out_of_range(ai, aj)):
            if empty_analisor(state[ai][aj]): possible_moves.append((ai, aj))
            if enemy_analisor(color, state[ai][aj]): possible_moves.append((ai, aj))
    return possible_moves


def king_detector(color, n):
    if color == "w":
        if n == "k":
            return True
    elif color == "b":
        if n == "K":
            return True
    return False


def list_add_position(list_move, i, j):
    for element in range(len(list_move)):
        if len(list_move[element]) == 2:
            list_move[element] = (i, j, list_move[element][0], list_move[element][1])
    return list_move


def mate_check(state, color):
    temp_movements = []
    total_movements = []
    for i in range(1, 9):
        for j in range(1, 9):
            if color == "b":
                if king_detector(color, state[i][j]):
                    king_bi, king_bj = i, j
                if enemy_analisor("b", state[i][j]):
                    if state[i][j] == "b":
                        temp_movements.append(list_add_position(pices_caller(state, i, j, "w", Bishop), i, j))
                    elif state[i][j] == "p":
                        temp_movements.append(list_add_position(pices_caller(state, i, j, "w", Pawn), i, j))
                    elif state[i][j] == "k":
                        temp_movements.append(list_add_position(pices_caller(state, i, j, "w", Knight), i, j))
                    elif state[i][j] == "r":
                        temp_movements.append(list_add_position(pices_caller(state, i, j, "w", Rook), i, j))
                    elif state[i][j] == "s":
                        temp_movements.append(list_add_position(pices_caller(state, i, j, "w", King), i, j))
                    elif state[i][j] == "q":
                        temp_movements.append(list_add_position(pices_caller(state, i, j, "w", Queen), i, j))

            elif color == "w":
                if king_detector(color, state[i][j]):
                    king_wi, king_wj = i, j
                if enemy_analisor("w", state[i][j]):
                    if state[i][j] == "B":
                        temp_movements.append(list_add_position(pices_caller(state, i, j, "b", Bishop), i, j))
                    elif state[i][j] == "P":
                        temp_movements.append(list_add_position(pices_caller(state, i, j, "b", Pawn), i, j))
                    elif state[i][j] == "K":
                        temp_movements.append(list_add_position(pices_caller(state, i, j, "b", Knight), i, j))
                    elif state[i][j] == "R":
                        temp_movements.append(list_add_position(pices_caller(state, i, j, "b", Rook), i, j))
                    elif state[i][j] == "S":
                        temp_movements.append(list_add_position(pices_caller(state, i, j, "b", King), i, j))
                    elif state[i][j] == "Q":
                        temp_movements.append(list_add_position(pices_caller(state, i, j, "b", Queen), i, j))

                    # for list_element in range(len(temp_movements)):
                    # for element in range(len(temp_movements[list_element])):
                    # 	if len(temp_movements[list_element][element]) == 2:
                    # 		total_movements.append((i, j, temp_movements[list_element][element][0],temp_movements[list_element][element][1]))
    return temp_movements

print(mate_check(statebase, "b"))
print(len(mate_check(statebase, "b")))



# print(Pawn(statebase,7,1,"w"))
# 1
