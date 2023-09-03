'''
The Game of Life written in object oriented fashion.
'''

# pylint: disable=too-few-public-methods
class Life():
    '''
    Very simple class to contain our implementation.

    We will have two methods. One that returns a value, and one that prints the
    value to stdout.

    We could have implemented this as classmethods as well, and may do so in the
    future.
    '''
    def __init__(self):
        self.board = [[]]

class Board():
    '''
    Class represents the board or "field". It should be able to do the 
    following:
    1. Store a board in a 2d list of list (maybe we could use an array)
    2. Read a board definition from a file, where, '*' indicates a live cell,
    and '.' indicates a dead cell.
    3. Print a reperesentation of the boards state, with the above definitions
    of '*' and '.'
    4. Based on the rules of the Game of Life, create a new board for the next
    generation.
    '''

    def __init__(self):
        '''
        Just set some default values
        '''
        self.board = []
        self.width = self.height = 0

    def read_file(self, filename):
        '''
        Read the board definition file its raw form
        '''
        # The "line.strip()" is probably un-needed as long as we take care of
        # our input.

        # We use "with" to handle resource leaks and excessive coding on our
        # part
        with open(filename, encoding='utf-8') as golfile:
            lines = [line.strip() for line in golfile]

        return lines

    def populate_board(self, raw):
        '''
        Get height and width, then convert raw into a 2d representation (list
        of list)
        '''
        h_w = raw.pop(0).split()
        self.set_height_and_width(h_w)
        self.compile_board_array(raw)

    def set_height_and_width(self, h_w):
        '''
        Consume height and width
        '''
        self.height = int(h_w[0])
        self.width = int(h_w[1])

    def compile_board_array(self, raw):
        '''
        Convert string representation to an actual 2d array
        '''
        self.board = []
        for row in raw:
            outrow = []
            for col in str(row):
                outrow.append(col)
            self.board.append(outrow)

    def load_from_file(self, filename):
        '''
        Read a raw representation from file then populate the instance 
        variables
        '''
        raw = self.read_file(filename)
        self.populate_board(raw)

    def display(self):
        '''
        Simply print the board to stdout
        '''
        for row in range(0, self.height):
            for col in range(0, self.width):
                print(self.board[row][col], end='')
            print()

    def compute_next(self):
        '''
        Compute the next generation board
        '''
        nextgen = Board()
        nextgen.height = self.height
        nextgen.width = self.width
        for row in range(0, self.height):
            outrow= []
            for col in range(0, self.width):
                square = self.calculate_square(col, row)
                outrow.append(square)
            nextgen.board.append(outrow)

        return nextgen

    # pylint: disable=invalid-name
    def calculate_square(self, x, y):
        '''
        Calculate a particular x, y square
        '''
        # A lookup table that describes deltas from x, y
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

        nextgen = '.'
        if self.board[y][x] == "*":
            if count in [2, 3]:
                nextgen = '*'
        else:
            if count == 3:
                nextgen = "*"

        return nextgen
