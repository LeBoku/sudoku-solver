""" solves a board"""

from collections import OrderedDict


def solve_board(board):
    """ solves a board """
    while not is_solved(board):
        distribution = get_number_distribution(board)

        for number in distribution.keys():
            if solve_by_number(board, number):
                break

        yield board


def solve_by_number(board, number):
    """ trys to solve the sudoku by checking for possible positions for the given number """
    squares = get_squares_without_number(board, number)
    for square in squares:
        posibilities = [cell for cell in get_empty_cells(
            square) if could_cell_contain(cell, number)]

        if len(posibilities) == 1:
            posibilities[0].value = number
            return True

    return False


def get_squares_without_number(board, number):
    """ gets all sqares not containing the given number """
    squares = board.squares
    return [square for square in squares.values() if not are_cells_containing(square, number)]


def are_cells_containing(cells, number):
    """ checks if any cell contains the number  """
    return any(cell.value == number for cell in cells)


def could_cell_contain(cell, number):
    """ checks if a cell could contain the given number """
    return are_cells_containing(cell.row + cell.column, number)


def get_empty_cells(cells):
    """ gets all cells with the value of 0 """
    return [cell for cell in cells if cell.value == 0]


def get_number_distribution(board):
    """ gets the occurence of all numbers on a board """
    distribution = {i: 0 for i in range(board.size + 1)}

    for cell in board.cells:
        distribution[cell.value] += 1

    distribution.pop(0)
    distribution = {number: count for number,
                    count in distribution.items() if count != board.size}

    return OrderedDict(sorted(distribution.items(), key=lambda t: t[1], reverse=True))


def is_solved(board):
    """ checks if a board is solved """
    for cell in board.cells:
        if cell.value == 0:
            return False

    return True
