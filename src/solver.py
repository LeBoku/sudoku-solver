""" solves a board"""

from collections import OrderedDict

from board import Board


def is_solved(board: Board):
    """ checks if a board is solved """
    for cell in board.cells:
        if cell.value == 0:
            return False

    return True


def solve_board(board: Board):
    """ solves a board """
    solving_order = OrderedDict({
        "almost full groups": solve_by_almost_full_groups,
        "most occuring number": solve_by_most_occuring_number,
        "implicit occupation": solve_by_implicit_occupation
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
            print_defeat_message(board, set_cell_count)
            break
    else:
        print_victory_message(set_cell_count)


def solve_by_almost_full_groups(board: Board):
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


def solve_by_most_occuring_number(board: Board):
    """ trys to solve the sudoku by checking possible positions for the most occuring numbers """
    set_cell = None
    distribution = get_number_distribution(board)

    for number in distribution.keys():
        squares = get_groups_without_number(board.squares, number)

        for square in squares:
            empty_cells = get_empty_cells(square)
            posibilities = [
                cell for cell in empty_cells if could_cell_contain(cell, number)]

            if len(posibilities) == 1:
                posibilities[0].value = number
                set_cell = posibilities[0]
                break

        if set_cell is not None:
            break

    return set_cell


def solve_by_implicit_occupation(board: Board):
    """ trys to solve by implicit occupation """
    set_cell = None
    distribution = get_number_distribution(board)

    for number in distribution.keys():
        number = 8
        occupied_groups = dict(rows=[], columns=[], squares=[])
        cells_groups_without_number = []

        group_types = dict(squares=board.squares,
                           rows=board.rows,
                           columns=board.columns)

        for group_type_name, group_type in group_types.items():
            for group in get_groups_without_number(group_type, number):
                empty_cells = get_empty_cells(group)
                possible_cells = [cell for cell in empty_cells
                                  if could_cell_contain(cell, number)]

                current_cell_group = dict(
                    type=group_type_name, cells=possible_cells)
                filter_cell_group(current_cell_group, occupied_groups)
                # don't filter group by filters originated by it 

                simularities = get_simularities_for_cells(possible_cells)

                for simularity_type, group_index in simularities.items():
                    if simularity_type is not group_type_name and group_index is not None:
                        occupied_groups[simularity_type].append(group_index)

                        for cell_group_without_number in cells_groups_without_number:
                            filter_cell_group(
                                cell_group_without_number, occupied_groups)
                            # check for new occupied groups

                cells_groups_without_number.append(current_cell_group)

            for cell_group in cells_groups_without_number:
                if len(cell_group["cells"]) == 1:
                    set_cell = cell_group["cells"][0]
                    set_cell.value = number
                    break
            
            if set_cell:
                break

        if set_cell is not None:
            break

    return set_cell


def filter_cell_group(cell_group, filters):
    """ filter cells by rows, columns and squares """
    filters = {name: value if name !=
               cell_group["type"] else [] for name, value in filters.items()}

    cell_group["cells"] = [cell for cell in cell_group["cells"]
                           if not(cell.row_index in filters["rows"]
                                  or cell.column_index in filters["columns"]
                                  or cell.square_index in filters["squares"])]


def get_simularities_for_cells(cells):
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


def get_groups_without_number(groups, number):
    """ gets all sqares not containing the given number """
    return [group for group in groups.values() if not are_cells_containing(group, number)]


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
