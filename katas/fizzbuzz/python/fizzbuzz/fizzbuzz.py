'''
The FizzBuzz kata written in object oriented fashion.
'''

import re

class FizzBuzz():
    '''
    Very simple class to contain our implementation.

    We could have implemented this as classmethods as well, and may do so in the
    future.
    '''

    def translate(self, number):
        '''
        From kata ---
        For any number print the number, unless:
        For multiples of three print “Fizz” instead of the number and for the
        multiples of five print “Buzz”. For numbers which are multiples of both
        three and five print “FizzBuzz “.
        '''
        value = ""

        if number % 3 == 0:
            value = "Fizz"

        if number % 5 == 0:
            value += "Buzz"

        if not value:
            value = f'{number}'

        return value

    def translate2(self, number):
        '''
        From kata (part 2) ---
        As before, but
        A number is fizz if it is divisible by 3 or if it has a 3 in it
        A number is buzz if it is divisible by 5 or if it has a 5 in it

        For exemple :

        53 should return FizzBuzz (contain 5 and 3)
        35 should return FizzBuzzBuzz (contain 3 and 5 and it divided by 5)
        '''
        value = ""

        if re.search('3', f'{number}'):
            value += "Fizz"

        if re.search('5', f'{number}'):
            value += "Buzz"

        if number % 3 == 0:
            value += "Fizz"

        if number % 5 == 0:
            value += "Buzz"

        if not value:
            value = f'{number}'

        return value
