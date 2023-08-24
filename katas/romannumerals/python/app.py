'''
Roman Numeral kata app
'''

from roman.roman import Roman

def main():
    '''
    Thin layer to exercise Roman class.

    It verifies two way translation for numbers up to 3000.
    '''
    toromancollector = {}
    todigitcollector = {}
    number = Roman()
    for i in range(1, 3001):
        romanize = number.toroman(i)
        toromancollector[number] = romanize
        digitize = number.todigits(romanize)
        todigitcollector[romanize] = digitize
        print(todigitcollector[romanize], toromancollector[number])
        assert todigitcollector[romanize] == digitize
        assert toromancollector[number] == romanize

if __name__ == "__main__":
    main()
