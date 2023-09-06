'''
The Mastermind kata written in object oriented fashion.
'''

import random

class Mastermind():
    '''
    Very simple class to contain our implementation.

    We will have two methods. One that returns a value, and one that prints the
    value to stdout.

    We could have implemented this as classmethods as well, and may do so in the
    future.
    '''
    def __init__(self):
        self.secret = []

    def set_secret(self, secret):
        '''
        Manually set secret
        '''
        self.secret = secret

    def get_secret(self):
        '''
        Get secret
        '''
        return self.secret

    def gen_secret(self, size, colors):
        '''
        Randomly set secret
        '''
        secret = []
        for dummy in range(0, size):
            color = random.choice(colors)
            secret.append(color)

        self.secret = secret

    def compare_guess_to_secret(self, guess, secret):
        '''
        Compare a guess to the secret.
        '''
