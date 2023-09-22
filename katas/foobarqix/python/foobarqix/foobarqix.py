# coding=utf-8
"""
The FooBarQix kata written in object oriented fashion.
"""

import re

class Number():
    '''
    Super class for Foo, Bar and Qix
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
        value = (not self.number % self.divisor) and self.word or ""
        print("value", value)
        return value

    def subst(self, digit):
        '''
        Test condition by comparing dictionary look up table.
        :return: self.word if conditions pass, "" otherwise
        '''
        value = (int(digit) == self.divisor) and self.word or ""
        return value

class Foo(Number):
    '''
    Class to represent numbers evenly divisible by 3
    '''
    def __init__(self, number):
        super().__init__(number, 3, "Foo")


class Bar(Number):
    '''
    Class to represent numbers evenly divisible by 3
    '''
    def __init__(self, number):
        super().__init__(number, 5, "Bar")


class Qix(Number):
    '''
    Class to represent numbers evenly divisible by 7
    '''
    def __init__(self, number):
        super().__init__(number, 7, "Qix")


class FooBarQix():
    """
    Very simple class to contain our implementation.

    We could have implemented this as classmethods as well, and may do so in the
    future.
    """

    def number_divide(self, number):
        """
        Check disivability of number under consideration. Build string 
        representing the divisability.
        """
        value = ""

        if number % 3 == 0:
            value = "Foo"

        if number % 5 == 0:
            value += "Bar"

        if number % 7 == 0:
            value += "Qix"

        return value

    def digit_substitution(self, number):
        """
        Per kata rules, substitute word for number where needed
        """
        value = ""
        for digit in str(number):
            if digit == "3":
                value += "Foo"

            if digit == "5":
                value += "Bar"

            if digit == "7":
                value += "Qix"

        return value

    def number_divide3(self, number):
        """
        Check disivability of number under consideration. Build string
        representing the divisability.
        """
        value = Foo(number).get_value() + Bar(number).get_value() + Qix(number).get_value()

        return value

    def digit_substitution3(self, number):
        """
        Per kata rules, substitute word for number where needed
        """
        value = ""
        for digit in str(number):
            value += Foo(number).subst(digit)
            value += Bar(number).subst(digit)
            value += Qix(number).subst(digit)
        return value

    def digit_substitution2(self, value):
        """
        Per kata step 2, substitute words for numbers and 0 with * as needed.
        If substitutions have been made, remove any other digits.

        For a different strategy, we will use regular expression substitution.
        """
        value = re.sub('3', "Foo", value)
        value = re.sub('5', "Bar", value)
        value = re.sub('7', "Fix", value)
        value = re.sub('0', "*", value)
        if not re.match('[0-9]', value):
            value = re.sub('[0-9]', "", value)

        return value

    def translate1(self, number):
        """
        From kata ---
        For any number print the number, unless:
        If the number is divisible by 3, write “Foo” instead of the number
        If the number is divisible by 5, add “Bar”
        If the number is divisible by 7, add “Qix”
        For each digit 3, 5, 7, add “Foo”, “Bar”, “Qix” in the digits order.
        """
        value = self.number_divide(number)
        value += self.digit_substitution(number)

        if not value:
            value = str(number)

        return value

    def translate2(self, number):
        """
        From kata (part 2) ---
        As before, but
        We have a new business request: we must keep a trace of 0 in numbers, 
        each 0 must be replaced by char “*”.

        101   => 1*1
        303   => FooFoo*Foo
        105   => FooBarQix*Bar
        10101 => FooQix**

        The test cases implies that We do the division substitutions first.
        Then iterate over the numbers making the digit substitutions, removing
        arbitrary numbers if a substitution has been made.
        That is
            101 => 101
            101 => 1*1

            303 => Foo303
            Foo303 = FooFoo*Foo

            105 => FooBarQix105
            FooBarQix105 => FooBarQix*Bar

            10101 => FooQix10101
            FooQix10101 =>FooQix**
        """
        # This gets the prefix
        value = self.number_divide(number) + str(number)
        # 303 => Foo303

        # Sub translation for number
        value = self.digit_substitution2(value)

        return value

    def translate3(self, number):
        """
        From kata ---
        Same as translate1, but using if reduction.
        If the number is divisible by 3, write “Foo” instead of the number
        If the number is divisible by 5, add “Bar”
        If the number is divisible by 7, add “Qix”
        For each digit 3, 5, 7, add “Foo”, “Bar”, “Qix” in the digits order.
        """
        value = self.number_divide3(number)
        for digit in str(number):
            value += self.digit_substitution3(digit)

        if not value:
            value = str(number)

        return value
