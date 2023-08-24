'''
The Roman Numeral kata written in object oriented fashion.
'''

TO_ROMAN_LUT = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    30: "XXX",
    20: "XX",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I"
}

TO_DIGITS_LUT = {
    "M" : 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL" : 40,
    "XXX": 30,
    "XX": 20,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "III": 3,
    "II": 2,
    "I": 1
}

class Roman():
    '''
    Very simple class to contain our implementation.
    '''


    def todigits(self, numeral):
        '''
        Convert roman representation to digits
        '''
        digits = 0
        remaining = numeral
        while remaining:
            for value, replace in TO_DIGITS_LUT.items():
                if remaining.startswith(value):
                    digits += replace
                    print(remaining, value, digits)
                    remaining = remaining.replace(value, '', 1)

        return digits

    def toroman(self, number):
        '''
        Convert digits to roman representation
        '''
        letters = ""
        remaining = number
        while remaining:
            for value, replace in TO_ROMAN_LUT.items():
                if remaining >= value:
                    letters += replace
#                    print(remaining, value, letters)
                    remaining -= value
                    break

        return letters
