"""
contains test-case boards in array form
most of them generated by http://www.websudoku.com
"""


EASY_BOARD = [
    0, 0, 0, 0, 0, 0, 0, 2, 7,
    0, 7, 4, 0, 0, 0, 6, 0, 5,
    8, 2, 0, 7, 5, 4, 0, 1, 0,
    0, 4, 0, 0, 7, 0, 0, 0, 1,
    6, 3, 5, 0, 0, 0, 7, 9, 2,
    1, 0, 0, 0, 2, 0, 0, 6, 0,
    0, 5, 0, 9, 3, 1, 0, 4, 6,
    4, 0, 1, 0, 0, 0, 5, 3, 0,
    3, 6, 0, 0, 0, 0, 0, 0, 0,
]


MEDIUM_BOARD = [
    0, 5, 9, 2, 0, 0, 4, 0, 0,
    6, 0, 3, 0, 7, 0, 0, 0, 5,
    8, 0, 7, 0, 0, 0, 2, 0, 0,
    0, 9, 0, 0, 0, 8, 0, 0, 0,
    0, 6, 0, 3, 0, 5, 0, 9, 0,
    0, 0, 0, 9, 0, 0, 0, 5, 0,
    0, 0, 5, 0, 0, 0, 3, 0, 9,
    4, 0, 0, 0, 9, 0, 1, 0, 7,
    0, 0, 1, 0, 0, 2, 5, 6, 0,
]

MEDIUM_BOARD_2 = [
    0, 7, 0, 0, 0, 0, 0, 9, 5,
    0, 0, 9, 0, 0, 4, 3, 0, 0,
    0, 0, 0, 0, 0, 8, 1, 2, 0,
    0, 0, 2, 0, 6, 0, 0, 1, 0,
    7, 0, 0, 9, 0, 2, 0, 0, 4,
    0, 5, 0, 0, 7, 0, 9, 0, 0,
    0, 6, 5, 1, 0, 0, 0, 0, 0,
    0, 0, 7, 8, 0, 0, 2, 0, 0,
    8, 9, 0, 0, 0, 0, 0, 6, 0,
]

MEDIUM_BOARD_3 = [
    2, 0, 5, 3, 6, 0, 1, 0, 0,
    6, 0, 0, 7, 0, 0, 2, 0, 0,
    0, 4, 7, 1, 0, 0, 0, 6, 0,
    0, 7, 6, 0, 4, 0, 0, 0, 0,
    9, 0, 0, 0, 0, 0, 0, 0, 6,
    0, 0, 0, 0, 9, 0, 8, 1, 0,
    0, 6, 0, 0, 0, 8, 4, 7, 0,
    0, 0, 4, 0, 0, 6, 0, 0, 9,
    0, 0, 9, 0, 7, 3, 0, 0, 1,
]


HARD_BOARD = [
    9, 0, 0, 4, 0, 0, 5, 7, 1,
    0, 0, 0, 0, 5, 0, 9, 0, 0,
    0, 1, 0, 0, 7, 0, 0, 0, 0,
    5, 0, 0, 0, 0, 0, 7, 6, 0,
    0, 0, 0, 8, 1, 7, 0, 0, 0,
    0, 2, 8, 0, 0, 0, 0, 0, 4,
    0, 0, 0, 0, 2, 0, 0, 5, 0,
    0, 0, 6, 0, 9, 0, 0, 0, 0,
    3, 9, 7, 0, 0, 5, 0, 0, 2,
]


HARDEST_BOARD = [
    0, 0, 0, 2, 1, 0, 0, 0, 0,
    0, 0, 7, 3, 0, 0, 0, 0, 0,
    0, 5, 8, 0, 0, 0, 0, 0, 0,
    4, 3, 0, 0, 0, 0, 0, 0, 0,
    2, 0, 0, 0, 0, 0, 0, 0, 8,
    0, 0, 0, 0, 0, 0, 0, 7, 6,
    0, 0, 0, 0, 0, 0, 2, 5, 0,
    0, 0, 0, 0, 0, 7, 3, 0, 0,
    0, 0, 0, 0, 9, 8, 0, 0, 0,
]

EVIL_BOARD = [
    5, 0, 9, 6, 0, 0, 0, 0, 4,
    0, 0, 0, 0, 5, 0, 0, 3, 1,
    0, 6, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 2, 9, 0, 0, 0, 0, 5,
    0, 0, 7, 1, 0, 4, 8, 0, 0,
    9, 0, 0, 0, 0, 7, 4, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 5, 0,
    7, 9, 0, 0, 8, 0, 0, 0, 0,
    1, 0, 0, 0, 0, 5, 9, 0, 3,
]


# http://www.telegraph.co.uk/news/science/science-news/9359579/Worlds-hardest-sudoku-can-you-crack-it.html
HARDEST_BOARD_2 = [
    8, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 3, 6, 0, 0, 0, 0, 0,
    0, 7, 0, 0, 9, 0, 2, 0, 0,
    0, 5, 0, 0, 0, 7, 0, 0, 0,
    0, 0, 0, 0, 4, 5, 7, 0, 0,
    0, 0, 0, 1, 0, 0, 0, 3, 0,
    0, 0, 1, 0, 0, 0, 0, 6, 8,
    0, 0, 8, 5, 0, 0, 0, 1, 0,
    0, 9, 0, 0, 0, 0, 4, 0, 0,
]

EMPTY_BOARD = [
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
]
