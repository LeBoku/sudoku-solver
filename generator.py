""" generators for boards """

from random import choice

from board import Board


def generate_board(size):
    """ generates for boards """
    board = Board(size)

    posibilities = [i + 1 for i in range(size)]

    rows = board.rows
    columns = board.columns
    squares = board.squares

    for cell in board.cells:
        row = [c.value for c in rows[cell.pos_vertical]]
        column = [c.value for c in columns[cell.pos_horizontal]]
        square = [c.value for c in squares[cell.square]]

        cell_posibilities = [
            possibility for possibility in posibilities if possibility not in row + column + square]

        if len(cell_posibilities) >= 1:
            cell.value =  choice(cell_posibilities)
    return board
