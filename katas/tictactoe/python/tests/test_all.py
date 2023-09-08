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

    def test_print_board(self):
        '''
        Intent:
        Test simple board display.
        '''
        cut = TTT()
        assert cut.print_board() == ""
