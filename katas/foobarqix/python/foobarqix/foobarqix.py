# coding=utf-8
"""
The FooBarQix kata written in object oriented fashion.
"""

import re

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

    def translate(self, number):
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
            value = "{number}"

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
