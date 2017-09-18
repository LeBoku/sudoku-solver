""" solves a board"""

from collections import OrderedDict

from board import Board


def solve_board(board: Board):
    """ solves a board """
    solving_order = OrderedDict({
        "Almost full groups": solve_by_almost_full_groups,
        "Most occuring number": solve_by_most_occuring_number
    })

    set_cell_count = 0

    while not is_solved(board):
        yield board
        for method, solver in solving_order.items():
            set_cell = solver(board)
            if set_cell is not None:
                print_solving_result(set_cell, method)
                set_cell_count += 1
                break
        else:
            print("No more cells can be set")
            print(f"Managed to set {set_cell_count} cell(s)")
            print(f"{len(get_empty_cells(board.cells))} cell(s) remain unset")

            break


def solve_by_almost_full_groups(board):
    """ trys to solve the board by filling almost full groups """
    set_cell = None

    to_ceck = list(
        board.rows.values()) +\
        list(board.columns.values()) +\
        list(board.squares.values())

    for cell_group in to_ceck:
        empty_cells = get_empty_cells(cell_group)

        if len(empty_cells) == 1:
            empty_cells[0].value = get_unused_numbers(board, cell_group)[0]
            set_cell = empty_cells[0]
            break

    return set_cell


def solve_by_most_occuring_number(board):
    """ trys to solve the sudoku by checkingpossible positions for the most occuring numbers """
    distribution = get_number_distribution(board)
    set_cell = None

    for number in distribution.keys():
        set_cell = solve_by_number(board, number)
        if set_cell is not None:
            break

    return set_cell


def solve_by_number(board, number):
    """ trys to place the given number for a cell """
    squares = get_squares_without_number(board, number)
    set_cell = None

    for square in squares:
        empty_cells = get_empty_cells(square)
        posibilities = [
            cell for cell in empty_cells if could_cell_contain(cell, number)]

        if len(posibilities) == 1:
            posibilities[0].value = number
            set_cell = posibilities[0]
            break

    return set_cell


def get_squares_without_number(board, number):
    """ gets all sqares not containing the given number """
    squares = board.squares
    return [square for square in squares.values() if not are_cells_containing(square, number)]


def are_cells_containing(cells, number):
    """ checks if any cell contains the number  """
    return any(cell.value == number for cell in list(cells))


def could_cell_contain(cell, number):
    """ checks if a cell could contain the given number """
    return not are_cells_containing(cell.row + cell.column + cell.square, number)


def get_empty_cells(cells):
    """ gets all cells with the value of 0 """
    return [cell for cell in cells if cell.value == 0]


def get_unused_numbers(board, cells):
    """ gets all the unused numbers in a cell group """
    possibilities = board.possibilities

    for cell in cells:
        if cell.value != 0:
            possibilities.remove(cell.value)

    return possibilities


def get_number_distribution(board):
    """ gets the occurence of all numbers on a board """
    distribution = {i: 0 for i in range(board.size + 1)}

    for cell in board.cells:
        distribution[cell.value] += 1

    distribution.pop(0)
    distribution = {number: count for number,
                    count in distribution.items() if count != board.size}

    return OrderedDict(sorted(distribution.items(), key=lambda t: t[1], reverse=True))


def print_solving_result(cell, method):
    """ log that and how a cell was filled """
    print(f"solved cell {cell.pos} with {cell.value} by {method}")


def is_solved(board):
    """ checks if a board is solved """
    for cell in board.cells:
        if cell.value == 0:
            return False

    return True
