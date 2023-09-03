'''
Test for Game of Life kata.
'''
import os

from life.life import Life, Board

BOARD1 = os.getcwd() + "\\" + "tests\\data\\board1.gol"

# pylint: disable=too-few-public-methods
class TestLife:
    '''
    Simple class to bundle our test under.
    '''

    def test_create(self):
        '''
        Intent:
        As a matter of style, always test that the class under test can create an 
        object.
        '''
        cut = Life()
        assert isinstance(cut, Life)

class TestBoard:
    '''
    Simple class to bundle our test under.
    '''

    def test_create(self):
        '''
        Intent:
        As a matter of style, always test that the class under test can create an 
        object.
        '''
        cut = Board()
        assert isinstance(cut, Board)
        assert cut.height == 0
        assert cut.width == 0

    def test_read_file(self):
        '''
        Simply test that read_file does not fail
        '''
        cut = Board()
        assert cut.read_file(BOARD1)

    def test_set_height_and_width(self):
        '''
        Simply that height and width get set
        '''
        cut = Board()
        cut.set_height_and_width(['4', '2'])
        assert cut.height == 4
        assert cut.width == 2

    def test_compile_board_array(self):
        '''
        Make sure we can create a full 2d table
        '''
        cut = Board()
        cut.compile_board_array(['.*.', '.*.', '.*.'])
        assert cut.board == [['.', '*', '.'], ['.', '*', '.'], ['.', '*', '.']]

    def test_load_from_file(self):
        '''
        load_from_file is a thin wrapper to read a raw board from a file and convert it to a 2d 
        representation
        '''
        cut = Board()
        cut.load_from_file(BOARD1)
        assert cut.height == 3
        assert cut.width == 3
        assert cut.board == [['.', '*', '.'], ['.', '*', '.'], ['.', '*', '.']]

    def test_display(self, capsys):
        '''
        Test that we can display a board to stdout
        '''
        cut = Board()
        cut.load_from_file(BOARD1)
        cut.display()
        captured = capsys.readouterr()
        assert captured.out == ".*.\n" + \
                               ".*.\n" + \
                               ".*.\n"

    def test_compute_next1(self):
        '''
        Test that we can compute next generation of the board
        '''
        cut = Board()
        cut.load_from_file(BOARD1)
        nextgen = cut.compute_next()
        assert nextgen.board == [['.', '.', '.'], ['*', '*', '*'], ['.', '.', '.']]
