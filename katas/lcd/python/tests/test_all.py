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

    def test_gen_lcd_digit_0_to_9(self):
        '''
        Generate an LCD digit
        '''
        cut = LCD()
        lcd_digit = cut.gen_lcd_digit(0)
        print(lcd_digit)
        assert lcd_digit == ' _ \n' \
                            '| |\n' \
                            '|_|\n'
        lcd_digit = cut.gen_lcd_digit(1)
        assert lcd_digit == '   \n'+\
                            '  |\n'+\
                            '  |\n'
        lcd_digit = cut.gen_lcd_digit(2)
        assert lcd_digit == ' _ \n'+\
                            ' _|\n'+\
                            '|_ \n'
        lcd_digit = cut.gen_lcd_digit(3)
        assert lcd_digit == ' _ \n'+\
                            ' _|\n'+\
                            ' _|\n'
        lcd_digit = cut.gen_lcd_digit(4)
        assert lcd_digit == '   \n'+\
                            '|_|\n'+\
                            '  |\n'
        lcd_digit = cut.gen_lcd_digit(5)
        assert lcd_digit == ' _ \n'+\
                            '|_ \n'+\
                            ' _|\n'
        lcd_digit = cut.gen_lcd_digit(6)
        assert lcd_digit == ' _ \n'+\
                            '|_ \n'+\
                            '|_|\n'
        lcd_digit = cut.gen_lcd_digit(7)
        assert lcd_digit == ' _ \n'+\
                            '  |\n'+\
                            '  |\n'
        lcd_digit = cut.gen_lcd_digit(8)
        assert lcd_digit == ' _ \n'+\
                            '|_|\n'+\
                            '|_|\n'
        lcd_digit = cut.gen_lcd_digit(9)
        assert lcd_digit == ' _ \n'+\
                            '|_|\n'+\
                            ' _|\n'

    def test_gen_lcd_number_mix(self):
        '''
        Generate an LCD number of multiple digits
        '''
        cut = LCD()
        lcd_number = cut.gen_lcd_number(42)
        assert lcd_number == '     _ \n'+\
                             '|_|  _|\n'+\
                             '  | |_ \n'
