""" Classes to Represent the state of the Sudoku board """

import math
from collections import OrderedDict


class Board:
    """ A Sudoku-board """

    def __init__(self, size=9):
        self.size = size
        self.square_size = 3
        self.square_count = size // self.square_size
        self.cells = [Cell(self, 0, i % size + 1, (i // size) + 1)
                      for i in range(size * size)]

    @classmethod
    def by_cell_array(cls, cell_array):
        """ sets up a board by a cell array """
        board = cls()
        for value, cell in zip(cell_array, board.cells):
            cell.value = value

        return board

    @property
    def possibilities(self):
        """ returns all the possible numbers on this board """
        return [i + 1 for i in range(self.size)]

    @property
    def rows(self):
        """ returns the cells grouped by rows """
        rows = {i + 1: [] for i in range(self.size)}

        for cell in self.cells:
            rows[cell.row_index].append(cell)

        return rows

    @property
    def columns(self):
        """ returns the cells grouped by collumns """
        columns = {i + 1: [] for i in range(self.size)}

        for cell in self.cells:
            columns[cell.column_index].append(cell)

        return columns

    @property
    def squares(self):
        """ returns the cells grouped by squares """
        squares = {(i % 3 + 1, i // 3 + 1): [] for i in range(self.size)}

        for cell in self.cells:
            squares[cell.square_index].append(cell)

        return squares

    def get_empty_cells(self):
        """ returns all the empty cells on the board """
        return [cell for cell in self.cells if cell.value == 0]

    def is_solved(self):
        """ checks if a board is solved """
        for cell in self.cells:
            if cell.value == 0:
                return False

        return True

    def is_valid(self):
        """ validates the board """
        for cell in self.cells:
            if(cell.value != 0):
                if not cell.could_contain(cell.value):
                    return False

        return True

    def get_number_distribution(self):
        """ gets the occurence of all numbers on a board """
        distribution = {number: 0 for number in self.possibilities}

        for cell in self.cells:
            if cell.value != 0:
                distribution[cell.value] += 1

        distribution = {number: count for number,
                        count in distribution.items() if count != self.size}

        return OrderedDict(sorted(distribution.items(), key=lambda t: t[1], reverse=True))


class Cell:
    """ A Cell on a Sudoku Board """

    def __init__(self, board, value, x, y):
        self.board = board
        self.value = value
        self.pos = x, y

    def could_contain(self, number):
        """ checks if a cell could contain """
        return not any([cell for cell in self.row + self.column + self.square
                        if cell is not self and cell.value == number])

    def get_possible_numbers(self):
        """ gets all the numbers that could be contained in this cell """
        return set([number for number in self.board.possibilities if self.could_contain(number)])

    @property
    def row_index(self):
        """ vertical position of a cell """
        return self.pos[1]

    @property
    def column_index(self):
        """ horizontal position of a cell """
        return self.pos[0]

    @property
    def square_index(self):
        """ square position of a cell """
        return (math.ceil(self.pos[0] / 3), math.ceil(self.pos[1] / 3))

    @property
    def row(self):
        """ row position of a cell """
        return self.board.rows[self.row_index]

    @property
    def column(self):
        """ column position of a cell """
        return self.board.columns[self.column_index]

    @property
    def square(self):
        """ square of a cell """
        return self.board.squares[self.square_index]
