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
        self.board = [[None, None, None], [None, None, None], [None, None, None]]
        self.player = "O"

    def get_board(self):
        '''
        Print the current board to stdout.
        '''
        return self.board

    def set_board(self, board):
        '''
        Print the current board to stdout.
        '''
        self.board = board
        return self.board

    def rotate_player(self):
        if self.player == "X":
            self.player = "O"
        else:
            self.player = "X"

        return self.player

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
        for line in self.board:
            print(line)
        return ''

    def make_move(self, square):
        '''
        Print the current board to stdout.
        '''
        dummy = square
        return ''

    def check_row_winner(self):
        '''
        Check for winners of a row
        '''
        winner = None
        row = None
        for i, row in enumerate(self.board):
            if row.count('X') == 3:
                winner = 'X'
                break
            if row.count('O') == 3:
                winner = 'O'
                break

        return [winner, i]

    def check_col_winner(self):
        '''
        Check for winners of a row
        '''
        winner = None
        col = None
        count = 0
        transpose = list(map(list, zip(*self.board)))

        for i, row in enumerate(transpose):
             if row.count('X') == 3:
                 winner = 'X'
                 break

             if row.count('O') == 3:
                 winner = 'O'
                 break

        return [winner, i]

    def check_end_of_game_and_winner(self):
        '''
        Check end of game conditions and report winner if available
        '''
        eog = False
        winner = None
        return [eog, winner]