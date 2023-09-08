'''
Test for Tic Tac Toe kata.
'''

from ttt.ttt import TTT

class TestTTT:
    '''
    Simple class to bundle our test under.
    '''

    def test_create(self):
        '''
        Intent:
        As a matter of style, always test that the class under test can create an 
        object.
        '''
        cut = TTT()
        assert isinstance(cut, TTT)

    def test_get_board(self):
        '''
        Intent:
        Any new TicTacToe game should start with an empty board.
        '''
        cut = TTT()
        assert cut.get_board() == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def test_accept_play(self):
        '''
        Intent:
        Test simple board display.
        '''
        cut = TTT()
        cut.accept_play(5)
        assert cut.get_board() == [[0, 0, 0], [0, "X", 0], [0, 0, 0]]
        cut.accept_play(7)
        assert cut.get_board() == [[0, 0, 0], [0, "X", 0], ["O", 0, 0]]

    def test_print_board(self):
        '''
        Intent:
        Test simple board display.
        '''
        cut = TTT()
        assert cut.print_board() == ""
