""" superclass for all Solvers """
from board import Board


class Solver:
    """ superclass for solvers"""

    def __init__(self, board: Board):
        self.set_cell_count = 0
        self.solving_method = ""
        self.board = board
        self.solved_cells_count = 0

    def solve(self):
        """ trys to solve the board """
        raise NotImplementedError

    def get_empty_cells(self, cells):
        """ gets all cells with the value of 0 """
        cells = cells if cells is not None else self.board.cells

        return [cell for cell in cells if cell.value == 0]

    def get_unused_numbers(self, cells):
        """ gets all the unused numbers in a cell group """
        possibilities = self.board.possibilities

        for cell in cells:
            if cell.value != 0:
                possibilities.remove(cell.value)

        return possibilities

    def get_groups_without_number(self, groups, number):
        """ gets all sqares not containing the given number """
        return [group for group in groups.values() if not self.are_cells_containing(group, number)]

    def are_cells_containing(self, cells, number):
        """ checks if any cell contains the number  """
        return any(cell.value == number for cell in list(cells))

    def could_cell_contain(self, cell, number):
        """ checks if a cell could contain the given number """
        return not self.are_cells_containing(cell.row + cell.column + cell.square, number)

    def get_possible_numbers(self, cells):
        """ gets all the numbers witch could be in the given cells """
        possible_numbers = set()

        for cell in cells:
            if cell.value == 0:
                possible_numbers.update(cell.get_possible_numbers())

        return possible_numbers
