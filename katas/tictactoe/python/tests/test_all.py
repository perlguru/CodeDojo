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
        assert cut.get_board() == [[None, None, None],
                                   [None, None, None],
                                   [None, None, None]]

    def test_accept_play(self):
        '''
        Intent:
        Test simple board display.
        '''
        cut = TTT()
        cut.accept_play(5)
        assert cut.get_board() == [[None, None, None],
                                   [None, "X", None],
                                   [None, None, None]]
        cut.accept_play(7)
        assert cut.get_board() == [[None, None, None],
                                   [None, "X", None],
                                   ["O", None, None]]

    def test_print_board(self):
        '''
        Intent:
        Test simple board display.
        '''
        cut = TTT()
        assert cut.print_board() == ""

    def test_check_end_of_game_and_winner(self):
        '''
        Intent:
        Check the top level end of game and winner conditions.

        Other test will check the individual conditions.
        '''
        cut = TTT()
        assert cut.check_end_of_game_and_winner() == [False, None]
        cut.accept_play(5)
        cut.accept_play(7)
        cut.accept_play(4)
        cut.accept_play(9)
        cut.accept_play(6)
        cut.print_board()
        assert cut.check_end_of_game_and_winner() == [True, 'X']

    def test_check_row_winner(self):
        '''
        Intent:
        Check the row winner conditions.
        '''
        cut = TTT()
        cut.set_board([[None, None, None], ["X", "X", "X"], [None, None, None]])
        assert cut.check_row_winner() == [1, 'X']
        cut.set_board([["O", "O", "O"], [None, None, None], [None, None, None]])
        assert cut.check_row_winner() == [0, 'O']

    def test_check_col_winner(self):
        '''
        Intent:
        Check the col winner conditions.
        '''
        cut = TTT()
        cut.set_board([[None, "X", None], [None, "X", None], [None, "X", None]])
        assert cut.check_col_winner() == [1, 'X']
        cut.set_board([["O", None, None], ["O", None, None], ["O", None, None]])
        assert cut.check_col_winner() == [0, 'O']

    def test_check_dia_winner(self):
        '''
        Intent:
        Check the col winner conditions.
        '''
        cut = TTT()
        cut.set_board([["X", None, None], [None, "X", None], [None, None, "X"]])
        assert cut.check_dia_winner() == [True, 'X']
        cut.set_board([[None, None, "O"], [None, "O", None], ["O", None, None]])
        assert cut.check_dia_winner() == [True, 'O']
