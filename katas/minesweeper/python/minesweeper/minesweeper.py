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
        with open(filename, encoding="utf-8") as msfile:
            lines = [line.rstrip() for line in msfile]

        return lines

    def set_height_and_width(self, h_w):
        '''
        extract height and width
        '''
        self.height = int(h_w[0])
        self.width = int(h_w[1])


    def compile_2d_array(self, raw):
        '''
        Convert string representation to an actual 2d array
        '''
        board = []
        for row in raw:
            outrow = []
            for col in str(row):
                outrow.append(col)
            board.append(outrow)
        return board

    def set_board(self, raw):
        '''
        From our string representation, get height, width and a 2d array of the
        board
        '''
        # Consume height and width
        self.set_height_and_width(raw.pop(0).split())
        self.board = self.compile_2d_array(raw)

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
            try:
                if self.board[y + square[1]][x + square[0]] == "*":
                    count += 1
            except IndexError:
                pass

        return count

    def print_solved(self):
        '''
        Just print it out
        '''
        for row in range(0, self.height):
            print("".join(str(value) for value in self.solved[row]))
