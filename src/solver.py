""" solves a board """

from board import Board
from solvers import AlmostFullGroupSolver, \
    MostOccuringNumberSolver, \
    ImplicitOccupationSolver, \
    ExclusionSolver, \
    BruteForceSolver \



def solve_board(board: Board):
    """ solves a board """

    brute_force_solver = BruteForceSolver(board)

    solvers = [
        AlmostFullGroupSolver(board),
        MostOccuringNumberSolver(board),
        ImplicitOccupationSolver(board),
        ExclusionSolver(board),
        brute_force_solver
    ]

    set_cell_count = 0

    while not board.is_solved():
        yield board

        for solver in solvers:
            set_cell = brute_force_solver.reset_if_needed()

            if set_cell is None:
                try:
                    set_cell = solver.solve()
                except IndexError:
                    set_cell = brute_force_solver.reset_if_needed(False)

            if set_cell is not None:
                print_solving_result(set_cell, solver.solving_method)
                solver.solved_cells_count += 1
                set_cell_count += 1
                break
        else:
            print_defeat_message(board)
            break

    else:
        print_victory_message()

    print_stats(set_cell_count, solvers)


def print_stats(set_cell_count, solvers):
    """ prints stats about the current state of the solving process """
    print(f"managed to set {set_cell_count} cell(s)")
    for solver in solvers:
        solver.print_stats()


def print_defeat_message(board):
    """ admits defeat but prints accomplishments """
    print("no more cells can be set")
    print(f"{len(board.get_empty_cells())} cell(s) remain unset")


def print_victory_message():
    """ declares victory and prints some facts """
    print("all cells set!")


def print_solving_result(cell, method):
    """ log that and how a cell was filled """
    print(f"solved cell {cell.pos} with {cell.value} by {method}")
