""" solves a board """

from board import Board
from solvers import AlmostFullGroupSolver, MostOccuringNumberSolver, ImplicitOccupationSolver, ExclusionSolver


def solve_board(board: Board):
    """ solves a board """

    solvers = [
        AlmostFullGroupSolver(board),
        MostOccuringNumberSolver(board),
        ImplicitOccupationSolver(board),
        ExclusionSolver(board)
    ]

    set_cell_count = 0

    while not board.is_solved():
        yield board
        for solver in solvers:
            set_cell = solver.solve()
            if set_cell is not None:
                print_solving_result(set_cell, solver.solving_method)
                set_cell_count += 1
                break
        else:
            print_defeat_message(board, set_cell_count)
            break
    else:
        print_victory_message(set_cell_count)


def get_empty_cells(cells):
    """ gets all cells with the value of 0 """
    return [cell for cell in cells if cell.value == 0]


def print_defeat_message(board, set_cell_count):
    """ admits defeat but prints accomplishments """
    print("no more cells can be set")
    print(f"managed to set {set_cell_count} cell(s)")
    print(f"{len(get_empty_cells(board.cells))} cell(s) remain unset")


def print_victory_message(set_cell_count):
    """ declares victory and prints some facts """
    print("all cells set!")
    print(f"managed to set {set_cell_count} cell(s)")


def print_solving_result(cell, method):
    """ log that and how a cell was filled """
    print(f"solved cell {cell.pos} with {cell.value} by {method}")
