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

    def test_compare_guess_to_secret_all_correct(self):
        '''
        Compare a guess to secret
        '''
        cut = Mastermind()
        cut.set_secret(['red', 'blue', 'green'])
        cut.set_guess(['red', 'blue', 'green'])
        assert cut.compare_guess_to_secret()
        assert cut.compare_guess_to_secret(guess=['red', 'blue', 'green']) == [3, 0]
        assert cut.compare_guess_to_secret(secret=['red', 'blue', 'green']) == [3, 0]
        assert cut.compare_guess_to_secret(guess=['red', 'blue', 'green'],
                                           secret=['red', 'blue', 'green']) == [3, 0]

    def test_compare_guess_to_secret_all_misplaced(self):
        '''
        Compare a guess to secret
        '''
        cut = Mastermind()
        cut.set_secret(['red', 'blue', 'green'])
        cut.set_guess(['blue', 'green', 'red'])
        assert cut.compare_guess_to_secret()
        assert cut.compare_guess_to_secret(guess=['blue', 'green', 'red']) == [0, 3]
        assert cut.compare_guess_to_secret(secret=['red', 'blue', 'green']) == [0, 3]
        assert cut.compare_guess_to_secret(guess=['blue', 'green', 'red'],
                                           secret=['red', 'blue', 'green']) == [0, 3]

    def test_compare_guess_to_secret_mixed(self):
        '''
        Compare a guess to secret
        '''
        cut = Mastermind()
        cut.set_secret(['red', 'blue', 'green'])
        cut.set_guess(['blue', 'blue', 'blue'])
        assert cut.compare_guess_to_secret() == [1, 0]
        assert cut.compare_guess_to_secret(guess=['blue', 'blue', 'red']) == [1, 1]
        assert cut.compare_guess_to_secret(secret=['red', 'blue', 'green']) == [1, 0]
        assert cut.compare_guess_to_secret(guess=['blue', 'blue', 'red'],
                                           secret=['red', 'blue', 'green']) == [1, 1]
        assert cut.compare_guess_to_secret(guess=['blue', 'blue', 'green'],
                                           secret=['red', 'blue', 'green']) == [2, 0]
        assert cut.compare_guess_to_secret(guess=['red', 'blue', 'red'],
                                           secret=['red', 'blue', 'green']) == [2, 0]
        assert cut.compare_guess_to_secret(guess=['blue', 'blue', 'blue'],
                                           secret=['red', 'blue', 'green']) == [1, 0]
        assert cut.compare_guess_to_secret(guess=['blue', 'blue', 'blue', 'blue'],
                                           secret=['red', 'blue', 'blue', 'green']) == [2, 0]
        assert cut.compare_guess_to_secret(guess=['blue', 'blue', 'blue', 'blue'],
                                           secret=['red', 'blue', 'green', 'blue']) == [2, 0]
        assert cut.compare_guess_to_secret(guess=['blue', 'blue', 'blue', 'green'],
                                           secret=['red', 'blue', 'green', 'blue']) == [1, 2]
