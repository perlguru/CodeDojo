'''
Test for FizzBuzz kata
'''

from fizzbuzz.fizzbuzz import FizzBuzz

class TestFizzBuzz:
    '''
    Simple class to bundle our test under.
    '''

    def test_create(self):
        '''
        Intent:
        As a matter of style, always test that the class under test can create
        an object.
        '''
        cut = FizzBuzz()
        assert isinstance(cut, FizzBuzz)

    def test_translate(self):
        '''
        Intent:
        Given any number we sholud be able to apply the FizzBuzz rules to get
        a string representation.

        For any number print the number, unless:
        For multiples of three print “Fizz” instead of the number and for the
        multiples of five print “Buzz”. For numbers which are multiples of both
        three and five print “FizzBuzz “.

        These test should be asily verifable by inspection.
        '''
        cut = FizzBuzz()
        assert cut.translate(1) == '1'
        assert cut.translate(3) == 'Fizz'
        assert cut.translate(5) == 'Buzz'
        assert cut.translate(15) == 'FizzBuzz'
        assert cut.translate(42) == 'Fizz'
        assert cut.translate(45) == 'FizzBuzz'
        assert cut.translate(49) == '49'
        assert cut.translate(50) == 'Buzz'

    def test_translate2(self):
        '''
        From kata (part 2) ---
        As before, but
        A number is fizz if it is divisible by 3 or if it has a 3 in it
        A number is buzz if it is divisible by 5 or if it has a 5 in it

        For exemple :

        53 should return FizzBuzz (contain 5 and 3)
        35 should return FizzBuzzBuzz (contain 3 and 5 and it divided by 5)
        '''
        cut = FizzBuzz()
        assert cut.translate2(1) == '1'
        assert cut.translate2(3) == 'FizzFizz'
        assert cut.translate2(5) == 'BuzzBuzz'
        assert cut.translate2(53) == 'FizzBuzz'
