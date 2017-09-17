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
            rows[cell.pos[1]].append(cell)

        return rows

    @property
    def columns(self):
        """ returns the cells grouped by rows """
        columns = [[] for i in range(self.size)]

        for cell in self.cells:
            columns[cell.pos[0]].append(cell)

        return columns


class Cell:
    """ A Cell on a Sudoku Board """

    def __init__(self, value, x, y):
        self.value = value
        self.pos = x, y
