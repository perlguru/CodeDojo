'''
Roman Numeral kata app
'''

from roman.roman import Roman

def main():
    '''
    Thin layer to exercise Hello class
    '''
    number = Roman()
    for i in range(1, 3001):
        print(number.toroman(i))

if __name__ == "__main__":
    main()
