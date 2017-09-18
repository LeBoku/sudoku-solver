""" Classes to Represent the state of the Sudoku board """

import math


class Board:
    """ A Sudoku-board """

    def __init__(self, size=9):
        self.size = size
        self.square_size = 3
        self.square_count = size // self.square_size
        self.cells = [Cell(self, 0, i % size + 1, (i // size) + 1)
                      for i in range(size * size)]

    @property
    def possibilities(self):
        """ returns all the possible numbers on this board """
        return [i + 1 for i in range(self.size)]

    @property
    def rows(self):
        """ returns the cells grouped by rows """
        rows = {i + 1: [] for i in range(self.size)}

        for cell in self.cells:
            rows[cell.pos_vertical].append(cell)

        return rows

    @property
    def columns(self):
        """ returns the cells grouped by collumns """
        columns = {i + 1: [] for i in range(self.size)}

        for cell in self.cells:
            columns[cell.pos_horizontal].append(cell)

        return columns

    @property
    def squares(self):
        """ returns the cells grouped by squares """
        squares = {(i // 3 + 1, i % 3 + 1): [] for i in range(self.size)}

        for cell in self.cells:
            squares[cell.square_index].append(cell)

        return squares


class Cell:
    """ A Cell on a Sudoku Board """

    def __init__(self, board, value, x, y):
        self.board = board
        self.value = value
        self.pos = x, y

    @property
    def pos_vertical(self):
        """ vertical position of a cell """
        return self.pos[1]

    @property
    def pos_horizontal(self):
        """ horizontal position of a cell """
        return self.pos[0]

    @property
    def square_index(self):
        """ square position of a cell """
        return (math.ceil(self.pos[0] / 3), math.ceil(self.pos[1] / 3))

    @property
    def row(self):
        """ row position of a cell """
        return self.board.rows[self.pos_vertical]

    @property
    def column(self):
        """ column position of a cell """
        return self.board.columns[self.pos_horizontal]

    @property
    def square(self):
        """ square of a cell """
        return self.board.squares[self.square_index]
