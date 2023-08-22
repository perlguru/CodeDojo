'''
Test for Leap Years kata
'''

from leapyear.leapyear import LeapYear

class TestLeapYear:
    '''
    Simple class to bundle our test under.
    '''

    def test_create(self):
        '''
        Intent:
        As a matter of style, always test that the class under test can create
        an object.
        '''
        cut = LeapYear()
        assert isinstance(cut, LeapYear)
