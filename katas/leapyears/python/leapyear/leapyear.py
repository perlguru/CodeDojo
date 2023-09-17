'''
The Leap Years kata written in object oriented fashion.
'''

from datetime import date

class LeapYear:
    '''
    Main LeapYear class
    '''

    def __init__(self, year):
        '''
        Simple constructor setting year.
        '''
        self.year = year

    def leapyear1(self):
        '''
        Method 1:
        Use the rules spelled out in kata.
        '''
        value = False

        if not self.year % 400:
            value = True

        if not self.year % 4:
            value = True

        if not self.year % 4 and self.year % 100:
            value = True

        if not self.year % 100 and self.year % 400:
            value = False

        if not self.year % 4000:
            value = False

        return value

    def leapyear1(self):
        '''
        Method 1:
        Use the rules spelled out in kata, but use defaultdict to avoid if's
        '''
        value = False

        if not self.year % 400:
            value = True

        if not self.year % 4:
            value = True

        if not self.year % 4 and self.year % 100:
            value = True

        if not self.year % 100 and self.year % 400:
            value = False

        if not self.year % 4000:
            value = False

        return value

    def leapyear2(self):
        '''
        Method 2:
        Simply use datetime.date to try to set date to year+2+29. Invalid dates
        should throw a ValueError Eception.
        '''
        value = False
        try:
            date(self.year, 2, 29)
            value = True
        except ValueError:
            value = False

        return value

