'''
The classic Hello world written in object-oriented fashion.
'''

class Hello():
    '''
    Very simple class to contain our implementation.

    We will have two methods. One that returns a value, and one that prints the
    value to stdout.

    We could have implemented this as class methods as well, and may do so in the
    future.
    '''

    def greeting(self):
        '''
        Get greeting value.
        '''
        return "Hello, world."

    def greet(self):
        '''
        Print greeting to stdout.
        '''
        print(self.greeting())
