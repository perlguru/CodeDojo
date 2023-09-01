'''
Test for Game of Life kata.
'''

from life.life import Life, Board

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

    def test_read_from_file(self):
        cut = Board()
        lines = cut.read_from_file("tests\\data\\board1.gol")
        assert lines == ""

    def test_convert_to_2d(self):
        assert False

    def test_display(self):
        assert False

    def test_create_next_gen(self):
        assert False
