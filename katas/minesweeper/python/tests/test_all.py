'''
Test for MineSweeper kata.
'''

from minesweeper.minesweeper import MineSweeper

BOARD1_SOLVED = '\
*100\n\
2210\n\
1*10\n\
1110\n'

class TestMineSweeper:
    '''
    Simple class to bundle our test under.
    '''

    def test_create(self):
        '''
        Intent:
        As a matter of style, always test that the class under test can create an
        object.
        '''
        cut = MineSweeper()
        assert isinstance(cut, MineSweeper)
        assert cut.height == 0
        assert cut.width == 0
        assert not cut.board
        assert not cut.solved


    def test_readfile(self):
        '''
        Just need to read the file
        '''
        cut = MineSweeper()
        lines = cut.readfile("tests\\data\\board1.ms")
        assert lines == ['4 4', '*...', '....', '.*..', '....']

    def test_set_board(self):
        '''
        Test that we can generate a 2d representation of the board
        '''
        cut = MineSweeper()
        cut.set_board(cut.readfile("tests\\data\\board1.ms"))

        assert cut.width == 4
        assert cut.height == 4
        assert cut.board ==  [['*', '.', '.', '.'], \
                              ['.', '.', '.', '.'], \
                              ['.', '*', '.', '.'], \
                              ['.', '.', '.', '.']]

    def test_calculate(self):
        '''
        Test that we can solve a simple puzzle
        '''
        cut = MineSweeper()
        cut.set_board(cut.readfile("tests\\data\\board1.ms"))
        cut.calculate()
        assert cut.solved == [['*',  1,   0,   0], \
                              [ 2,   2,   1,   0], \
                              [ 1, '*',   1,   0], \
                              [ 1,   1,   1,   0]]

    def test_print_solved(self, capsys):
        '''
        Not that interesting, but included for completeness.
        '''
        cut = MineSweeper()
        cut.set_board(cut.readfile("tests\\data\\board1.ms"))
        cut.calculate()
        cut.print_solved()
        captured = capsys.readouterr()
        assert captured.out == BOARD1_SOLVED

    def test_print_board1(self):
        cut = MineSweeper()
        cut.my_board()
        assert 1==0