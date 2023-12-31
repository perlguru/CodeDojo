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
        '''
        ...
        '''
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
        for i, row in enumerate(self.board):
            if row.count('X') == 3:
                winner = 'X'
                break

            if row.count('O') == 3:
                winner = 'O'
                break

        return [i, winner]

    def check_col_winner(self):
        '''
        Check for winners of a row
        '''
        winner = None
        transpose = list(map(list, zip(*self.board)))
        col = 0

        for i, row in enumerate(transpose):
            col = i
            if row.count('X') == 3:
                winner = 'X'
                break

            if row.count('O') == 3:
                winner = 'O'
                break

        return [col, winner]

    def check_dia_winner(self):
        '''
        ...
        '''
        winner = None
        count = 0
        dia_ul_lr = [self.board[0][0], self.board[1][1], self.board[2][2]]
        dia_ur_ll = [self.board[2][0], self.board[1][1], self.board[0][2]]
        for which in ["X", "O"]:
            count = dia_ul_lr.count(which)

            if count == 3:
                winner = which
                break

            count = dia_ur_ll.count(which)

            if count == 3:
                winner = which
                break

        if winner:
            return [True, winner]

        return [False, None]

    def check_eog(self):
        '''
        ...
        '''
        count = 0
        for dummy, row in enumerate(self.board):
            count += row.count(None)

        if count == 0:
            return True

        return False

    def check_end_of_game_and_winner(self):
        '''
        Check end of game conditions and report winner if available
        '''
        eog = False
        winner = None

        status = self.check_row_winner()
        if status[1]:
            eog = True
            winner = status[1]

        if not eog:
            status = self.check_col_winner()
            if status[1]:
                eog = True
                winner = status[1]

        if not eog:
            status = self.check_dia_winner()
            if status[1]:
                eog = True
                winner = status[1]

        if not eog:
            eog = self.check_eog()
            winner = None

        return [eog, winner]
