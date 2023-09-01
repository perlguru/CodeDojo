'''
The Game of Life written in object oriented fashion.
'''

class Life():
    '''
    Very simple class to contain our implementation.

    We will have two methods. One that returns a value, and one that prints the
    value to stdout.

    We could have implemented this as classmethods as well, and may do so in the
    future.
    '''
    def __init__(self):
        self.board = [[]]

class Board():
    '''
    Class represents the board or "field". It should be able to do the following:
    1. Store a board in a 2d list of list (maybe we could use an array)
    2. Read a board definition from a file, where, '*' indicates a life cell, and '.' indicates a dead cell.
    3. Print a reperesentation of the boards state, with the above definitions of '*' and '.'
    4. Based on the rules of the Game of Life, create a new board for the next generation.
    '''

    def __init__(self):
        pass

    def read_from_file(self, filename):
        pass

    def convert_to_2d(self):
        pass

    def display(self):
        pass

    def create_next_gen(self):
        pass
