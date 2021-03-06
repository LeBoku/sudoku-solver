""" trys to solve the board by checking if a number could be set somewhere
checks for all numbers in all cells of all squares if there is only one possible cell in the square
starts with the most likely number (the most occuring one)
"""

from .solver import Solver


class MostOccuringNumberSolver(Solver):
    """ trys to solve the board by checking if a number could be set somewhere """

    def __init__(self, board):
        super().__init__(board)
        self.solving_method = "most occuring number"

    def solve(self):
        """ trys to solve the board by checking if a number could be set somewhere """
        set_cell = None

        distribution = self.board.get_number_distribution()

        for number in distribution.keys():
            squares = self.get_groups_without_number(
                self.board.squares, number)

            for square in squares:
                empty_cells = self.get_empty_cells(square)
                posibilities = [
                    cell for cell in empty_cells if self.could_cell_contain(cell, number)]

                if len(posibilities) == 1:
                    posibilities[0].value = number
                    set_cell = posibilities[0]
                    break

            if set_cell is not None:
                break

        return set_cell
