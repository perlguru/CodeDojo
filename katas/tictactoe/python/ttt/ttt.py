'''
Tic Tac Toe written in object oriented fashion.
'''

class TTT():
    '''
    Very simple class to contain our implementation.
    '''

    def __init__(self):
        '''
        Initialize instance
        '''
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.player = "X"

    def get_board(self):
        '''
        Print the current board to stdout.
        '''
        return self.board

    def rotate_player(self):
        current = self.player

        if self.player == "X":
            self.player = "O"

        return current

    def accept_play(self, pos):

        '''
        Print the current board to stdout.
        '''
        line = int((pos - 1)/ 3)
        self.board[line][pos % 3 - 1] = self.rotate_player()

    def print_board(self):
        '''
        Print the current board to stdout.
        '''
        return ''

    def make_move(self, square):
        '''
        Print the current board to stdout.
        '''
        dummy = square
        return ''
