""" Visualization of a board """

import time

from generator import generate_board
from solver import solve_board
from board import Board

import test_boards

VERTICAL_DIVIDER = "|"
HORIZONTAL_DIVIDER = "---"


def show_board_in_cmd(board):
    """ shows the board in the cmd """

    for cell in board.cells:
        cell_display = cell.value if cell.value != 0 else "_"
        print(f" {cell_display} ", end="")

        if cell.column_index == board.size \
                and cell.row_index % board.square_size == 0\
                and cell.row_index is not board.size:
            print()
            print(*[board.square_size *
                    HORIZONTAL_DIVIDER for i in range(board.square_count)], sep="|")

        elif cell.column_index % board.size == 0:
            print()

        elif cell.column_index % board.square_size == 0:
            print("|", end="")


def display_solving_process(board):
    """ solves the sudoku and shows every step """
    for step in solve_board(board):
        show_board_in_cmd(step)
        print()
        # time.sleep(0.5)

    print("final state:")
    show_board_in_cmd(board)


if __name__ == "__main__":
    # display_solving_process(generate_board())
    # display_solving_process(Board.by_cell_array(test_boards.MEDIUM_BOARD_3))
    # display_solving_process(Board.by_cell_array(test_boards.HARDEST_BOARD_2))
    display_solving_process(Board.by_cell_array(test_boards.HARD_BOARD))
