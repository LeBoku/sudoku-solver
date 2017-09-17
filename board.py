""" Classes to Represent the state of the Sudoku board """


class Board:
    """ A Sudoku-board """

    def __init__(self, size):
        self.size = size
        self.cells = [Cell(0, i % size, (i // size))
                      for i in range(size * size)]

    @property
    def rows(self):
        """ returns the cells grouped by rows """
        rows = [[] for i in range(self.size)]

        for cell in self.cells:
            rows[cell.pos_vertical].append(cell)

        return rows

    @property
    def columns(self):
        """ returns the cells grouped by collumns """
        columns = [[] for i in range(self.size)]

        for cell in self.cells:
            columns[cell.pos_horizontal].append(cell)

        return columns

    @property
    def squares(self):
        """ returns the cells grouped by squares """
        squares = {(i // 3, i % 3): [] for i in range(self.size)}

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
        return (self.pos[0] // 3, self.pos[1] // 3)

    def __repr__(self):
        return self.pos + ": " + self.value
