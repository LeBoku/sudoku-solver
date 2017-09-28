""" generators for boards """

from random import choice

from board import Board


def generate_board(values_to_remove_count=60):
    """ generates for boards """
    size = 9
    board = Board(size)

    posibilities = [i + 1 for i in range(size)]

    cells_to_fill = board.cells.copy()

    while len(cells_to_fill) >= 1:
        cell = cells_to_fill.pop(0)

        row_values = [c.value for c in cell.row]
        column_values = [c.value for c in cell.column]
        square_values = [c.value for c in cell.square]

        used_values = set(row_values + column_values + square_values)

        cell_posibilities = [
            possibility for possibility in posibilities if possibility not in used_values]

        if len(cell_posibilities) >= 1:
            cell.value = choice(cell_posibilities)
        else:
            cells_to_fill.append(cell)

            for filled_cell in [c for c in choice([cell.row, cell.column, cell.square])
                                if c.value != 0]:
                filled_cell.value = 0
                cells_to_fill.append(filled_cell)

    remove_values(board, values_to_remove_count)

    return board


def remove_values(board, amount):
    """ removes the given amount of values from the board """
    for i in range(amount):
        while True:
            cell = choice(board.cells)

            if cell.value != 0:
                cell.value = 0
                break
