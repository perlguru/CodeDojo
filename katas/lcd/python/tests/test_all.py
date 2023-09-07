'''
Test for Number to LCD kata.
'''

from lcd.lcd import LCD

class TestLCD:
    '''
    Simple class to bundle our test under.
    '''

    def test_create(self):
        '''
        Intent:
        As a matter of style, always test that the class under test can create an 
        object.
        '''
        cut = LCD()
        assert isinstance(cut, LCD)

    def test_get_number(self):
        '''
        Simply our number gettor.
        '''
        cut = LCD()
        cut.arabic = 42
        assert cut.get_number() == 42


    def test_set_number(self):
        '''
        Simply set our working number.
        '''
        cut = LCD()
        cut.set_number(42)
        assert cut.arabic == 42
