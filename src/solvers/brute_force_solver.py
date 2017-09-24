""" trys to solve the board by strategically guessing """

from collections import namedtuple

from copy import deepcopy

from .solver import Solver
from .implicit_occupation_solver import IMPLICITLY_OCCUPIED_CELLS

GuessState = namedtuple(
    "GuessState", ["frozen_board", "guesses"])


class BruteForceSolver(Solver):
    """ trys to solve the board by strategically guessing """

    def __init__(self, board):
        super().__init__(board)
        self.solving_method = "guessing"
        self.reset_count = 0
        self.guess_states = []

    @property
    def has_guessed(self):
        """ checks if the current board has guessed cells on it """
        return len(self.guess_states) > 0

    def print_stats(self):
        """ prints the stats and the reset_count """
        super().print_stats()
        print(f"  and {self.reset_count} resets")

    def solve(self):
        """ trys to solve the board by strategically guessing """
        set_cell = None

        state = GuessState(self.board.serialzie_to_cell_array(), {})
        self.guess_states.append(state)

        set_cell = self.try_next_cell(state)

        return set_cell

    def try_next_cell(self, state):
        """ trys the next possible number/cell """
        set_cell = None

        cells_to_try = [cell for cell in self.board.get_empty_cells()
                        if cell not in list(state.guesses.keys())[:-1]]

        for cell in cells_to_try:
            if cell not in state.guesses.keys():
                state.guesses[cell] = set()

            tried_numbers = state.guesses[cell]

            numbers_to_try = [number for number in cell.get_possible_numbers()
                              if number not in tried_numbers]

            for number in numbers_to_try:
                tried_numbers.add(number)
                if cell not in IMPLICITLY_OCCUPIED_CELLS[number]:
                    cell.value = number
                    set_cell = cell
                    break

            if set_cell is not None:
                break

        return set_cell

    def reset_if_needed(self, check_for_validity=True):
        """ resets the guesses after a validity-check on the board
        or immediatly if check_for_for_valid = False
        """
        if self.has_guessed and (not check_for_validity or not self.board.is_valid()):
            print("reseting due to (now) invalid cells")
            return self.retry()

    def retry(self):
        """ resets the board to the last correct state and then trys the next number/cell """
        set_cell = None
        self.reset_count += 1
        self.reset_implicitly_occupied_cells()

        for state in reversed(self.guess_states):
            self.board.set_up_by_cell_array(state.frozen_board)
            set_cell = self.try_next_cell(state)

            if set_cell is not None:
                break

        return set_cell

    def reset_implicitly_occupied_cells(self):
        """ resets the implicitly occupied cells collection """
        for number in IMPLICITLY_OCCUPIED_CELLS:
            IMPLICITLY_OCCUPIED_CELLS[number] = set()
