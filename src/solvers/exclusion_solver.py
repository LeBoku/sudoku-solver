""" trys to solve the board by exclusion """

from .solver import Solver
from .implicit_occupation_solver import IMPLICITLY_OCCUPIED_CELLS

class ExclusionSolver(Solver):
    """ trys to solve the board by exclusion """

    def __init__(self, board):
        super().__init__(board)
        self.solving_method = "exclusion"

    def solve(self):
        """ trys to solve the board by exclusion """
        set_cell = None

        groups = list(self.board.squares.values()) + \
            list(self.board.rows.values()) + \
            list(self.board.columns.values())

        for group in groups:
            # empty_cells = self.get_empty_cells(self.board.squares[(2, 2)])
            empty_cells = self.get_empty_cells(group)

            if len(empty_cells) > 2:
                set_cell = self.check_for_exclusion(empty_cells)
                if set_cell is not None:
                    break

        return set_cell

    def check_for_exclusion(self, cells):
        """ checks cells if any can be solved by exclusion """
        set_cell = None
        number_possibilities = {number: []
                                for number in self.board.possibilities}

        for cell in cells:
            for number in cell.get_possible_numbers():
                if cell not in IMPLICITLY_OCCUPIED_CELLS[number]:
                    number_possibilities[number].append(cell)

        number_possibilities = {number: cells for number, cells in number_possibilities.items()
                                if len(cells) >= 1}

        groups = []

        if len(number_possibilities) > 2:
            for number, cells in number_possibilities.items():
                for group in groups:
                    added_to_group = False

                    for g_cells in group.values():
                        overlapping_cells = [
                            cell for cell in cells if cell in g_cells]
                        if len(overlapping_cells) >= 1:
                            group[number] = cells
                            added_to_group = True
                            break

                    if added_to_group:
                        break

                else:
                    groups.append({number: cells})

            possible_groups = [group for group in groups if len(group) > 2]

            for group in possible_groups:
                cell_references = {}
                for number, cells in group.items():
                    for cell in cells:
                        if cell not in cell_references.keys():
                            cell_references[cell] = []
                        cell_references[cell].append(number)

                cell_references = {cell: references for cell, references in cell_references.items()
                                   if len(references) == 1}

                if len(cell_references.keys()) == 1:
                    set_cell, numbers = cell_references.popitem()
                    set_cell.value = numbers[0]
                    break

            return set_cell
