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
        cell_possibilities = {}

        for cell in cells:
            cell_possibilities[cell] = []
            for number in cell.get_possible_numbers():
                if cell not in IMPLICITLY_OCCUPIED_CELLS[number]:
                    cell_possibilities[cell].append(number)

        groups = []

        if len(cell_possibilities) > 2:
            for cell, numbers in cell_possibilities.items():
                for group in groups:
                    added_to_group = False

                    for group_numbers in group.values():
                        overlapping_numbers = [
                            number for number in numbers if number in group_numbers]
                        if len(overlapping_numbers) >= 1:
                            group[cell] = numbers
                            added_to_group = True
                            break

                    if added_to_group:
                        break

                else:
                    groups.append({cell: numbers})

            possible_groups = [group for group in groups if all(
                [len(numbers) >= len(group) - 1 for numbers in group.values()])]

            for group in possible_groups:
                for cell, numbers in group.items():
                    for number in numbers:
                        if all([number in group_numbers for group_numbers in group.items()]):
                            for group_numbers in group.values():
                                group_numbers.remove(number)

                possible_groups = [group for group in possible_groups
                                   if all(len(numbers) == 1 for numbers in group.values())]

                if len(possible_groups) >= 1:
                    set_cell, numbers = possible_groups[0].popitem()
                    set_cell.value = numbers[0]
                    break

            return set_cell
