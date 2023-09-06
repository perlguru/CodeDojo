'''
Test for Mastermind kata.
'''

from mastermind.mastermind import Mastermind

class TestMastermind:
    '''
    Simple class to bundle our test under.
    '''

    def test_create(self):
        '''
        Intent:
        As a matter of style, always test that the class under test can create an 
        object.
        '''
        cut = Mastermind()
        assert isinstance(cut, Mastermind)

    def test_set_secret(self):
        '''
        Manually set secret
        '''
        cut = Mastermind()
        cut.set_secret(['red', 'blue', 'green'])
        assert cut.get_secret() == ['red', 'blue', 'green']

    def test_gen_secret(self):
        '''
        Generate an arbitrary secret
        '''
        cut = Mastermind()
        colors = ['red', 'blue', 'green']
        cut.gen_secret(4, colors)
        secret = cut.get_secret()

        assert len(secret) == 4
        valid = 0
        for color in colors:
            valid += secret.count(color)

        assert valid == 4

    def test_compare_guess_to_secret(self):
        '''
        Compare a guess to secret
        '''
        assert False