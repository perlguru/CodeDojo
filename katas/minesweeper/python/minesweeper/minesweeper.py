'''
The MineSweeper kata written in object oriented fashion.
'''

class MineSweeper():
    '''
    Very simple class to contain our implementation.
    '''
    def __init__(self):
        '''
        Just set some default values
        '''
        self.solved = []
        self.board = []
        self.width = 0
        self.height = 0

    def readfile(self, filename):
        '''
        Read the string representation from a file
        '''
        # pylint: disable=unspecified-encoding
        with open(filename) as msfile:
            lines = [line.rstrip() for line in msfile]

        return lines

    def set_board(self, raw):
        '''
        From our string representation, get height, width and a 2d array of the
        board
        '''
        # Consume height and width
        h_w = raw.pop(0).split()
        self.height = int(h_w[0])
        self.width = int(h_w[1])

        # Convert string representation to an actual 2d array
        self.board = []
        for row in raw:
            outrow = []
            for col in str(row):
                outrow.append(col)
            self.board.append(outrow)

    def calculate(self):
        '''
        Calculate the board
        '''
        for row in range(0, self.height):
            outrow= []
            for col in range(0, self.width):
                if self.board[row][col] == '*':
                    outrow.append("*")
                if self.board[row][col] == '.':
                    square = self.calculate_square(col, row)
                    outrow.append(square)
            self.solved.append(outrow)

        return self.solved

    # pylint: disable=invalid-name
    def calculate_square(self, x, y):
        '''
        Calculate a particular x, y square
        '''
        # A lookup table that describes deltas from out x, y
        square_lut = [[-1, -1], [0, -1], [1, -1], \
                      [-1,  0],          [1,  0], \
                      [-1,  1], [0,  1], [1,  1]]

        count = 0
        for square in square_lut:
            # Convience
            # pylint: disable=invalid-name
            dx = square[0]
            dy = square[1]

            # We don't want to check non-existant squares
            if dx + x >= 0 and dy + y >= 0 \
                and \
                dx + x <= self.width - 1 and dy + y <= self.height - 1:

                if self.board[y + dy][x + dx] == "*":
                    count += 1

        return count

    def print_solved(self):
        '''
        Just print it out
        '''
        for row in range(0, self.height):
            for col in range(0, self.width):
                print(self.solved[row][col], end='')
            print()
