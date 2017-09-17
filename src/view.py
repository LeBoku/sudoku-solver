""" Visualization of a board"""

from generator import generate_board


def show_board_in_cmd(board):
    """ shows the board in the cmd """
    for index, row in enumerate(board.rows):
        for cell_index, cell in enumerate(row):
            print(" " + str(cell.value if cell.value != 0 else "_") + " ", end="")

            if (cell_index + 1) % 3 == 0 and cell_index + 1 is not board.size:
                print("|", end="")

        print()

        if (index + 1) % 3 == 0 and index + 1 is not board.size:
            for i in range(board.size):
                print("---", end="")
                if(i + 1) % 3 == 0 and i + 1 is not board.size:
                    print("|", end="")
            print()


if __name__ == "__main__":
    show_board_in_cmd(generate_board())
