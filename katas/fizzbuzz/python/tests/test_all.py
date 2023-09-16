# coding=utf-8
"""
Test for FizzBuzz kata
"""

from fizzbuzz.fizzbuzz import FizzBuzz

class TestFizzBuzz:
    """
    Simple class to bundle our test under.
    """

    def test_create(self):
        """
        Intent:
        As a matter of style, always test that the class under test can create
        an object.
        """
        cut = FizzBuzz()
        assert isinstance(cut, FizzBuzz)

    def test_translate1(self):
        """
        Intent:
        Given any number we should be able to apply the FizzBuzz rules to get
        a string representation.

        For any number print the number, unless:
        For multiples of three print “Fizz” instead of the number and for the
        multiples of five print “Buzz”. For numbers which are multiples of both
        three and five print “FizzBuzz “.

        These test should be easily verifiable by inspection.
        """
        cut = FizzBuzz()
        assert cut.translate1(1) == '1'
        assert cut.translate1(3) == 'Fizz'
        assert cut.translate1(5) == 'Buzz'
        assert cut.translate1(15) == 'FizzBuzz'
        assert cut.translate1(42) == 'Fizz'
        assert cut.translate1(45) == 'FizzBuzz'
        assert cut.translate1(49) == '49'
        assert cut.translate1(50) == 'Buzz'

    def test_translate2(self):
        """
        From kata (part 2) ---
        As before, but
        A number is fizz if it is divisible by 3 or if it has a 3 in it
        A number is buzz if it is divisible by 5 or if it has a 5 in it

        For example :
        53 should return FizzBuzz (contain 5 and 3)
        35 should return FizzBuzzBuzz (contain 3 and 5, and it is divisible by 5)
        """
        cut = FizzBuzz()
        assert cut.translate2(1) == '1'
        assert cut.translate2(3) == 'FizzFizz'
        assert cut.translate2(5) == 'BuzzBuzz'
        assert cut.translate2(35) == 'FizzBuzzBuzz'
        assert cut.translate2(53) == 'FizzBuzz'

    def test_translate3(self):
        """
        Intent:
        Given any number we should be able to apply the FizzBuzz rules to get
        a string representation.

        For any number print the number, unless:
        For multiples of three print “Fizz” instead of the number and for the
        multiples of five print “Buzz”. For numbers which are multiples of both
        three and five print “FizzBuzz “.

        These test should be asily verifable by inspection.
        """
        cut = FizzBuzz()
        assert cut.translate3(1) == '1'
        assert cut.translate3(3) == 'Fizz'
        assert cut.translate3(5) == 'Buzz'
        assert cut.translate3(15) == 'FizzBuzz'
        assert cut.translate3(42) == 'Fizz'
        assert cut.translate3(45) == 'FizzBuzz'
        assert cut.translate3(49) == '49'
        assert cut.translate3(50) == 'Buzz'

    def test_translate4(self):
        cut = FizzBuzz()
        assert cut.translate4(1) == '1'
        assert cut.translate4(3) == 'Fizz'
        assert cut.translate4(5) == 'Buzz'
        assert cut.translate4(15) == 'FizzBuzz'
        assert cut.translate4(49) == '49'

    def test_translate5(self):
        assert FizzBuzz.translate5(1) == '1'
        assert FizzBuzz.translate5(3) == 'Fizz'
        assert FizzBuzz.translate5(5) == 'Buzz'
        assert FizzBuzz.translate5(15) == 'FizzBuzz'
        assert FizzBuzz.translate5(49) == '49'
