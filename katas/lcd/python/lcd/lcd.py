'''
Number to LCD written in object oriented fashion.
'''

class LCD():
    '''
    Very simple class to contain our implementation.
    '''

    # A Simple global to express our LCD digit representations
    LCD_DIGITS = [
        [' _ \n'+\
         '| |\n'+\
         '|_|'],
        ['   \n'+\
         '  |\n'+\
         '  |'],
        [' _\n'+\
         ' _|\n'+\
         '|_ '],
        [' _ \n'+\
         ' _|\n'+\
         ' _|'],
        ['   \n'+\
         '|_|\n'+\
         '  |'],
        [' _ \n'+\
         '|_ \n'+\
         ' _|'],
        [' _ \n'+\
         '|__\n'+\
         '|_|'],
        [' _ \n'+\
         '  |\n'+\
         '  |'],
        [' _ \n'+\
         '|_|\n'+\
         '|_|'],
        [' _ \n'+\
         '|_|\n'+\
         ' _|']
    ]

    def __init__(self):
        '''
        Initialize instance
        '''
        self.arabic = 0

    def set_number(self, number):
        '''
        Set the aribic number we will be using.

        We could verify that number is an integer. We will do that when needed.
        '''
        self.arabic = number

    def get_number(self):
        '''
        Get our working number.
        '''
        return self.arabic

    def gen_lcd_digit(self, digit):
        '''
        Generate a single LCD digit
        '''
        return "".join(self.LCD_DIGITS[digit])
