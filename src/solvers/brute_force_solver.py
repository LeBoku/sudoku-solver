""" trys to solve the board by strategically guessing """

from collections import namedtuple

from copy import deepcopy

from .solver import Solver
from .implicit_occupation_solver import IMPLICITLY_OCCUPIED_CELLS

GuessState = namedtuple(
    "GuessState", ["frozen_board", "cell", "guesses"])


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
        cell = self.get_most_populated_square()[0]

        state = GuessState(self.board.serialzie_to_cell_array(), cell, set())
        self.guess_states.append(state)

        set_cell = self.try_next_number(state)

        return set_cell

    def get_most_populated_square(self):
        """ get's the square with the most filled cells """

        most_filled = [0] * self.board.size

        for square in self.board.squares.values():
            empty_cells = self.get_empty_cells(square)
            empty_cells_count = len(empty_cells)
            if len(most_filled) > empty_cells_count and empty_cells_count != 0:
                most_filled = empty_cells

        return most_filled

    def try_next_number(self, state):
        """ trys the next possible number/cell """
        set_cell = None

        numbers_to_try = [number for number in state.cell.get_possible_numbers()
                          if number not in state.guesses and state.cell not in IMPLICITLY_OCCUPIED_CELLS[number]]

        for number in numbers_to_try:
            state.guesses.add(number)
            state.cell.value = number
            set_cell = state.cell
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
        """ resets the board to the last correct state and then trys the next number """
        set_cell = None
        self.reset_count += 1
        self.reset_implicitly_occupied_cells()

        for state in reversed(self.guess_states):
            self.board.set_up_by_cell_array(state.frozen_board)
            set_cell = self.try_next_number(state)

            if set_cell is None:
                self.guess_states.remove(state)
            else:
                break

        return set_cell

    def reset_implicitly_occupied_cells(self):
        """ resets the implicitly occupied cells collection """
        for number in IMPLICITLY_OCCUPIED_CELLS:
            IMPLICITLY_OCCUPIED_CELLS[number] = set()
