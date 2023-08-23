'''
Test for Leap Years kata
'''

import pytest

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
        cut = LeapYear(2000)
        assert isinstance(cut, LeapYear)

    def test_by_4(self):
        '''
        Test things that are divisable by 4
        '''
        cut = LeapYear(1992)
        assert cut.leapyear1() is True
        cut = LeapYear(1996)
        assert cut.leapyear1() is True
        cut = LeapYear(1999)
        assert cut.leapyear1() is False
        cut = LeapYear(2000)
        assert cut.leapyear1() is True
        cut = LeapYear(2001)
        assert cut.leapyear1() is False
        cut = LeapYear(2004)
        assert cut.leapyear1() is True
        cut = LeapYear(2008)
        assert cut.leapyear1() is True


    def test_by_100(self):
        '''
        Test things that are divisable by 100 (and divisable by 400)
        '''
        cut = LeapYear(1900)
        assert cut.leapyear1() is False
        cut = LeapYear(2000)
        assert cut.leapyear1() is True
        cut = LeapYear(2100)
        assert cut.leapyear1() is False

    def test_by_400(self):
        '''
        Test things that are divisable by 400 (and and not divisable by 100)
        '''
        cut = LeapYear(1900)
        assert cut.leapyear1() is False
        cut = LeapYear(2000)
        assert cut.leapyear1() is True
        cut = LeapYear(2100)
        assert cut.leapyear1() is False

    def test_by_4000(self):
        '''
        Test things that are divisable by 4000 (and and not divisable by 400)
        '''
        cut = LeapYear(1900)
        assert cut.leapyear1() is False
        cut = LeapYear(2000)
        assert cut.leapyear1() is True
        cut = LeapYear(2100)
        assert cut.leapyear1() is False
        cut = LeapYear(4000)
        assert cut.leapyear1() is False
        cut = LeapYear(8000)
        assert cut.leapyear1() is False
        cut = LeapYear(4100)
        assert cut.leapyear1() is False
        cut = LeapYear(8100)
        assert cut.leapyear1() is False

    def test2_by_4(self):
        '''
        Test things that are divisable by 100 (and divisable by 400)
        '''
        cut = LeapYear(1992)
        assert cut.leapyear2() is True
        cut = LeapYear(1996)
        assert cut.leapyear2() is True
        cut = LeapYear(1999)
        assert cut.leapyear2() is False
        cut = LeapYear(2000)
        assert cut.leapyear2() is True
        cut = LeapYear(2001)
        assert cut.leapyear2() is False
        cut = LeapYear(2004)
        assert cut.leapyear2() is True
        cut = LeapYear(2008)
        assert cut.leapyear2() is True


    def test2_by_100(self):
        '''
        Test things that are divisable by 100 (and divisable by 400)
        '''
        cut = LeapYear(1900)
        assert cut.leapyear2() is False
        cut = LeapYear(2000)
        assert cut.leapyear2() is True
        cut = LeapYear(2100)
        assert cut.leapyear2() is False

    def test2_by_400(self):
        '''
        Test things that are divisable by 400 (and and not divisable by 100)
        '''
        cut = LeapYear(1900)
        assert cut.leapyear2() is False
        cut = LeapYear(2000)
        assert cut.leapyear2() is True
        cut = LeapYear(2100)
        assert cut.leapyear2() is False

    def test2_by_4000(self):
        '''
        Test things that are divisable by 4000 (and and not divisable by 400)
        '''
        cut = LeapYear(1900)
        assert cut.leapyear2() is False
        cut = LeapYear(2000)
        assert cut.leapyear2() is True
        cut = LeapYear(2100)
        assert cut.leapyear2() is False
        cut = LeapYear(4100)
        assert cut.leapyear2() is False
        cut = LeapYear(8100)
        assert cut.leapyear2() is False

    @pytest.mark.xfail
    def test2_by_4000_python(self):
        '''
        Test things that are divisable by 4000 (and and not divisable by 400)
        Note python does not recognize year 4000 or 8000
        '''
        cut = LeapYear(4000)
        assert cut.leapyear2() is False
        cut = LeapYear(8000)
        assert cut.leapyear2() is False
