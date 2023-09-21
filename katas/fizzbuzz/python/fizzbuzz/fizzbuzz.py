# coding=utf-8
'''
The FizzBuzz kata written in object oriented fashion.
'''

import re

class Number():
    '''
    Super class for Fizz and Buzz
    '''
    def __init__(self, number, divisor, word):
        '''
        :param number: Number under inspection
        :param divisor: The effective divisor
        :param word: Replacement word, if needed
        '''
        self.number = number
        self.divisor = divisor
        self.word = word

    def get_value(self):
        '''
        Test condition by boolean comparison (not if's)
        :return: self.word if conditions pass, "" otherwise
        '''
        return (not self.number % self.divisor) and self.word or ""

    def lu_value(self):
        '''
        Test condition by comparing dictionary look up table.
        :return: self.word if conditions pass, "" otherwise
        '''
        value = {
            0 : self.word
        }

        key = self.number % self.divisor
        value.setdefault(key, "")

        return value[key]

class Fizz(Number):
    '''
    Class to represent numbers evenly divisible by 3
    '''
    def __init__(self, number):
        super().__init__(number, 3, "Fizz")

class Buzz(Number):
    '''
    Class to represent numbers evenly divisible by 5
    '''
    def __init__(self, number):
        super().__init__(number, 5, "Buzz")

class FizzBuzz():

    '''
    Very simple class to contain our implementation.

    We could have implemented this as classmethods as well, and may do so in the
    future.
    '''

    def translate1(self, number):
        '''
        From kata:
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

        # Maybe we could just set value to number or str(number) here?
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

        The kata does not describe how we should treat some thing like 535,
        so we ignore the problem and simply take the kata at its literal 
        translation
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

    def translate3(self, number):
        '''
        Using the same rules as translate1, lets use a lambda.
        '''
        # pylint: disable= unnecessary-lambda-assignment
        value = lambda i: 'Fizz'*(not i % 3)+'Buzz'*(not i % 5) or i

        return str(value(number))

    def translate4(self, number):
        '''
        Using the same rules as translate1, lets use individual classes to
        avoid if/then's.
        '''
        value = Fizz(number).lu_value() + Buzz(number).lu_value() or number

        return str(value)

    @classmethod
    def translate5(cls, number):
        '''
        From kata:
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

        # Maybe we could just set value to number or str(number) here?
        if not value:
            value = f'{number}'

        return value

    def translate6(self, number):
        '''
        Using the same rules as translate1, lets use individual classes to
        avoid if/then's.
        '''
        value = Fizz(number).get_value() + Buzz(number).get_value() or number

        return str(value)
