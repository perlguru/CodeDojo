'''
Test for Roman Numeral kata.
'''

from roman.roman import Roman

class TestHello:
    '''
    Simple class to bundle our test under.
    '''

    def test_create(self):
        '''
        Intent:
        As a matter of style, always test that the class under test can create an 
        object.
        '''
        cut = Roman()
        assert isinstance(cut, Roman)
