""" trys to solve the board by filling almost full groups
'almost full groups' means rows/columns/squares with 8 out of 9 cells filled
the last one can then be set by checking which number is missing
"""

from .solver import Solver


class AlmostFullGroupSolver(Solver):
    """ trys to solve the board by filling almost full groups """

    def __init__(self, board):
        super().__init__(board)
        self.solving_method = "almost full group"

    def solve(self):
        """ trys to solve the board by filling almost full groups """
        set_cell = None

        to_ceck = list(
            self.board.rows.values()) +\
            list(self.board.columns.values()) +\
            list(self.board.squares.values())

        for cell_group in to_ceck:
            empty_cells = self.get_empty_cells(cell_group)

            if len(empty_cells) == 1:
                empty_cells[0].value = self.get_unused_numbers(cell_group)[0]
                set_cell = empty_cells[0]
                break

        return set_cell
