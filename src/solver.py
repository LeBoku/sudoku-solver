""" solves a board"""

from collections import OrderedDict

from board import Board


def solve_board(board: Board):
    """ solves a board """
    while not is_solved(board):
        yield board

        if solve_by_almost_full_groups(board):
            continue

        distribution = get_number_distribution(board)

        for number in distribution.keys():
            if solve_by_number(board, number):
                break


def solve_by_almost_full_groups(board):
    """ trys to solve the board by filling almost full groups """

    to_ceck = list(
        board.rows.values()) +\
        list(board.columns.values()) +\
        list(board.squares.values())

    for cell_group in to_ceck:
        empty_cells = get_empty_cells(cell_group)
        if len(empty_cells) == 1:
            empty_cells[0].value = get_unused_numbers(board, cell_group)[0]
            print_solving_result(empty_cells[0], "almost full groups")
            return True


def solve_by_number(board, number):
    """ trys to solve the sudoku by checking for possible positions for the given number """
    squares = get_squares_without_number(board, number)
    for square in squares:
        empty_cells = get_empty_cells(square)
        posibilities = [cell for cell in empty_cells if could_cell_contain(cell, number)]

        if len(posibilities) == 1:
            posibilities[0].value = number

            print_solving_result(posibilities[0], "most used numbers")
            return True

    return False


def get_squares_without_number(board, number):
    """ gets all sqares not containing the given number """
    squares = board.squares
    return [square for square in squares.values() if not are_cells_containing(square, number)]


def are_cells_containing(cells, number):
    """ checks if any cell contains the number  """
    return any(cell.value == number for cell in list(cells))


def could_cell_contain(cell, number):
    """ checks if a cell could contain the given number """
    return not are_cells_containing(cell.row + cell.column + cell.square, number)


def get_empty_cells(cells):
    """ gets all cells with the value of 0 """
    return [cell for cell in cells if cell.value == 0]


def get_unused_numbers(board, cells):
    """ gets all the unused numbers in a cell group """
    possibilities = board.possibilities

    for cell in cells:
        if cell.value != 0:
            possibilities.remove(cell.value)

    return possibilities


def get_number_distribution(board):
    """ gets the occurence of all numbers on a board """
    distribution = {i: 0 for i in range(board.size + 1)}

    for cell in board.cells:
        distribution[cell.value] += 1

    distribution.pop(0)
    distribution = {number: count for number,
                    count in distribution.items() if count != board.size}

    return OrderedDict(sorted(distribution.items(), key=lambda t: t[1], reverse=True))


def print_solving_result(cell, method):
    """ log that and how a cell was filled """
    print(f"solved cell {cell.pos} with {cell.value} by {method}")


def is_solved(board):
    """ checks if a board is solved """
    for cell in board.cells:
        if cell.value == 0:
            return False

    return True
