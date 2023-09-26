"""
The MineSweeper kata written in object oriented fashion.
"""

import random

# A lookup table that describes deltas from our x, y
RING_LUT = [[-1, -1], [0, -1], [1, -1],
            [-1, 0],           [1,  0],
            [-1, 1],  [0,  1], [1,  1]]

class Board():
    """
    Class to contain a "board's" state, and provide operations on the board,
    such as statically setting a boards state, random generating a boards
    state, setting and getting individual tiles state, and calculating
    neighboring tiles exposure.
    """
    def __init__(self, rows=8, columns=8):
        """
        Basic Board constructor
        @param rows: Number of rows for board. Default 8.
        @param columns: Number of rows for board. Default 8.
        self.board: The generated board. Each tiles state defaults to None.
        """
        self.rows = rows
        self.columns = columns

        self.board = [[0 for x in range(columns)] for y in range(rows)]
        for i in range(rows):
            for j in range(columns):
                self.board[i][j] = None

    def set_size(self, h_w):
        """
        Extract height and width
        """
        self.rows = int(h_w[0])
        self.columns = int(h_w[1])

    def build(self, raw):
        """
        Convert string representation to an actual 2d array
        """
        board = []
        for row in raw:
            outrow = []
            for col in str(row):
                outrow.append(col)
            board.append(outrow)

        return board

    def randomize(self, rate=10):
        """
        Randomly populate a board.
        @param rate: Bomb rate in percentage of likely tiles. Default 10.
        Which means that approximately 10% of the tiles will be bombs
        """
        for row in range(0, self.rows):
            for col in range (0, self.columns):
                r = random.random()
                self.set_tile(row, col, r > rate / 100 and "." or "*")

    def display(self):
        """
        Display the board to stdout.
        """
        for y in range(0, self.columns):
            for x in range(0, self.rows):
                print(self.get_tile(x, y), end="")
            print()

    def get_tile(self, x, y):
        """
        Return the value of the tile at x, y
        @param x: Target column
        @param y: Target row
        @return: *, ., or count of adjoining bombs
        """
        return self.board[x][y]

    def set_tile(self, x, y, value):
        """
        Set the value of the tile at x, y
        @param x: Target column
        @param y: Target row
        """
        self.board[x][y] = value

    @staticmethod
    def readfile(filename):
        """
        Read the string representation from a file
        """
        with open(filename) as msfile:
            lines = [line.rstrip() for line in msfile]

        return lines

    def set_board(self, raw):
        """
        From our string representation, get height, width and a 2d array of the
        board
        """
        # Consume height and width
        self.set_size(raw.pop(0).split())
        self.board = self.build(raw)

    def calculate(self):
        """
        Calculate the board
        """
        solved = Board(self.rows, self.columns)
        x = 0
        for row in self.board:
            y = 0
            for col in row:
                value = col
                if col == '.':
                    value = self.calculate_square(y, x)
                solved.set_tile(x, y, value)
                y += 1
            x += 1

        self.solved = solved

        return self.solved

    # x and y make sense
    # pylint: disable=invalid-name
    def calculate_square(self, x, y):
        """
        Calculate a particular x, y square
        """
        count = 0
        for square in RING_LUT:
            try:
                if self.get_tile([y + square[1]][0], [x + square[0]][0]) == "*":
                    count += 1
            except IndexError:
                pass

        return count


    def print_solved(self):
        """
        Just print it out
        """
        for row in self.solved.board:
            print("".join(str(value) for value in row))


class MineSweeper():
    """
    Very simple class to contain our implementation.
    """
    def __init__(self, rows=8, columns=8):
        """
        Just set some default values
        @rtype: object
        """
        self._board = Board(rows, columns)
        self._solved = Board(rows, columns)

    def board(self):
        """
        Accessor for board object
        """
        return self._board

    def solved(self):
        """
        Accessor for solved object
        """
        return self._solved

    def gen_board(self, rate=10):
        """
        Randomly populate a preexisting board with a certain rate of mines.
        Also generates the solution board.
        @param rate: Rate of bombs. For example, 10 would be 10% bombs to
        90% safe tiles.
        @return: None
        """
        self._board.randomize(rate)
        self._solved = self.board().calculate()
