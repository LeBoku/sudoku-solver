""" generators for boards """

from random import choice

from board import Board


def generate_board():
    """ generates for boards """
    size = 9
    board = Board(size)

    posibilities = [i + 1 for i in range(size)]

    rows = board.rows
    columns = board.columns
    squares = board.squares

    cells_to_fill = board.cells.copy()

    while len(cells_to_fill) >= 1:
        cell = cells_to_fill.pop(0)

        row = rows[cell.pos_vertical]
        column = columns[cell.pos_horizontal]
        square = squares[cell.square]

        row_values = [c.value for c in row]
        column_values = [c.value for c in column]
        square_values = [c.value for c in square]

        used_values = set(row_values + column_values + square_values)

        cell_posibilities = [
            possibility for possibility in posibilities if possibility not in used_values]

        if len(cell_posibilities) >= 1:
            cell.value = choice(cell_posibilities)
        else:
            cells_to_fill.append(cell)
            to_reset = [
                c for c in choice([row, column, square]) if c.value != 0]

            for filled_cell in to_reset:
                filled_cell.value = 0
                cells_to_fill.append(filled_cell)

    return board
