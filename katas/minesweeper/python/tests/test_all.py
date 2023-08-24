'''
Test for MineSweeper kata.
'''

from minesweeper.minesweeper import MineSweeper

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

    def test_board(self):
        '''
        '''
        cut = MineSweeper()

    def test_board_with_values(self):
        '''
        '''
        cut = MineSweeper()
