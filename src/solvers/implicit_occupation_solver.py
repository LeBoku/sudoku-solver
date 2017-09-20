""" trys to solve by implicit occupation """

from .solver import Solver


class ImplicitOccupationSolver(Solver):
    """ trys to solve by implicit occupation """

    def __init__(self, board):
        super().__init__(board)
        self.solving_method = "implicit occupation"

    def solve(self):
        """ trys to solve by implicit occupation """
        set_cell = None
        distribution = self.board.get_number_distribution()

        for number in distribution.keys():
            occupied_cells = set()
            groups_without_number = []

            group_types = dict(squares=self.board.squares,
                               rows=self.board.rows,
                               columns=self.board.columns)

            for group_type_name, group_type in group_types.items():
                for group in self.get_groups_without_number(group_type, number):
                    possible_cells = self.get_empty_cells(group)
                    possible_cells = [cell for cell in possible_cells
                                      if self.could_cell_contain(cell, number)]

                    self.update_occupied_cells(
                        occupied_cells, possible_cells, group_type_name, groups_without_number)

                    groups_without_number.append(possible_cells)

                for cell_group in groups_without_number:
                    if len(cell_group) == 1:
                        set_cell = cell_group[0]
                        set_cell.value = number
                        break

                if set_cell:
                    break

            if set_cell is not None:
                break

        return set_cell

    def update_occupied_cells(self, occupied_cells, cells, group_type, groups_without_number):
        """ updates the occupied cells """
        self.filter_cell_group(cells, occupied_cells)
        newly_occupied = self.get_implicitly_occupied_cells(group_type, cells)

        if newly_occupied is not None:
            occupied_cells.update(newly_occupied)
            for group_without_number in groups_without_number:
                self.filter_cell_group(group_without_number, occupied_cells)

    def get_implicitly_occupied_cells(self, group_type, cells):
        """ adds occupied cells if possible """
        simularities = self.get_simularities_for_cells(cells)

        for simularity_type, group_index in simularities.items():
            if simularity_type is not group_type and group_index is not None:
                affected_cell_group = getattr(
                    self.board, simularity_type)[group_index]
                return [cell for cell in affected_cell_group if cell not in cells]

    def filter_cell_group(self, cell_group, filter_cells):
        """ filter cells by the given filter_cells """
        cell_group[:] = [
            cell for cell in cell_group if cell not in filter_cells]

    def get_simularities_for_cells(self, cells):
        """ checks if all the cells have the same row and/or column and/or square """
        first_cell = cells[0]

        row = first_cell.row_index
        column = first_cell.column_index
        square = first_cell.square_index

        for cell in cells[1:]:
            if row != cell.row_index:
                row = None

            if column != cell.column_index:
                column = None

            if square != cell.square_index:
                square = None

        return dict(rows=row, columns=column, squares=square)
