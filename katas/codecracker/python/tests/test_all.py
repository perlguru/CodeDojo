'''
Test for Code Cracker kata.
'''

from codecracker.codecracker import Decode, Encode

class TestCodeCracker:
    '''
    Simple class to bundle our test under.
    '''

    def test_create(self):
        '''
        Intent:
        As a matter of style, always test that the class under test can create an 
        object.
        '''
        cut = Decode()
        assert isinstance(cut, Decode)

        cut = Encode()
        assert isinstance(cut, Encode)
