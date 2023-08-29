'''
Test for Game of Life kata.
'''

from life.life import Life



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
