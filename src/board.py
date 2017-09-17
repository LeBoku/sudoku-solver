""" Classes to Represent the state of the Sudoku board """

import math


class Board:
    """ A Sudoku-board """

    def __init__(self, size=9):
        self.size = size
        self.square_size = 3
        self.square_count = size // self.square_size
        self.cells = [Cell(0, i % size + 1, (i // size) + 1)
                      for i in range(size * size)]

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
            squares[cell.square].append(cell)

        return squares


class Cell:
    """ A Cell on a Sudoku Board """

    def __init__(self, value, x, y):
        self.value = value
        self.pos = x, y

    @property
    def pos_vertical(self):
        """ horizontal position of a cell"""
        return self.pos[1]

    @property
    def pos_horizontal(self):
        """ vertical position of a cell"""
        return self.pos[0]

    @property
    def square(self):
        """ square position of a cell"""
        return (math.ceil(self.pos[0] / 3), math.ceil(self.pos[1] / 3))
