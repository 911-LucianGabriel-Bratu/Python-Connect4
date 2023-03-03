from domain.cell import Cell
from texttable import Texttable


class Board:
    """

    Board class
    >the board-type object takes the form of a 7x6 matrix in which every element is a Cell-type object
    >when printed, it displays on the console a texttable in which every element appears

    """
    def __init__(self):
        self.rows = 6
        self.columns = 7
        self.map = [[Cell() for i in range(self.columns)] for j in range(self.rows)]

    def __getitem__(self, item):
        return self.map[item]

    def __str__(self):
        t = Texttable()

        header = list(range(self.columns))
        t.header(['/', ""] + header)

        for row in range(self.rows):
            t.add_row([str(row), "|"] + self.map[row])
        return t.draw()
