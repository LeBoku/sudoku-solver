""" Visualization of a board"""

from generator import generate_board


def show_board_cmd(board):
    """ shows the board in the cmd """
    for row in board.rows:
        print(*[cell.value for cell in row], sep="  ")

if __name__ == "__main__":
    show_board_cmd(generate_board(9))
