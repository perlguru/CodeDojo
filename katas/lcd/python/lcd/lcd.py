'''
Number to LCD written in object oriented fashion.
'''

class LCD():
    '''
    Very simple class to contain our implementation.
    '''


    LCD_DIGITS = [
        [
         [0,2,0], #  _
         [1,0,1], # | |
         [1,2,1], # |_|
        ],
        [
         [0,0,0], #
         [0,0,1], #   |
         [0,0,1], #   |
        ],
        [
         [0,2,0], #  _
         [0,2,1], #  _|
         [1,2,0], # |_
        ],
        [
         [0,2,0], #  _
         [0,2,1], #  _|
         [0,2,1], #  _|
        ],
        [
         [0,0,0], # 
         [1,2,1], # |_|
         [0,0,1], #   |
        ],
        [
         [0,2,0], #  _
         [1,2,0], # |_
         [0,2,1], #  _|
        ],
        [
         [0,2,0], #  _
         [1,2,0], # |_
         [1,2,1], # |_|
        ],
        [
         [0,2,0], #  _
         [0,0,1], #   |
         [0,0,1], #   |
        ],
        [
         [0,2,0], #  _
         [1,2,1], # |_|
         [1,2,1], # |_|
        ],
        [
         [0,2,0], #  _
         [1,2,1], # |_|
         [0,2,1], #  _|
        ]
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
        definition = self.LCD_DIGITS[digit]
        final = ""
        for line in definition:
            out = ""
            for i in line:
                if i == 1:
                    out += "|"
                elif i == 2:
                    out += "_"
                else: 
                    out +=" "
            final += out + "\n"

        return final

    def gen_lcd_number(self, number):
        '''
        Generate a full LCD number
        '''
        for digit in list(str(number)):
            print(self.LCD_DIGITS[int(digit)])

        return list(str(number))
