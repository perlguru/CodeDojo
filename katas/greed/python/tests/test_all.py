'''
Test for Greed kata
'''

from greed.greed import Greed

class TestGreed:
    '''
    Simple class to bundle our test under.
    '''

    def test_create(self):
        '''
        Intent:
        As a matter of style, always test that the class under test can create
        an object.
        '''
        cut = Greed()
        assert isinstance(cut, Greed)
