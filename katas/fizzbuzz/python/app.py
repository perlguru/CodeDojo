'''
FizzBuzz kata application
'''

import cProfile

from fizzbuzz.fizzbuzz import FizzBuzz

def main():
    '''
    Thin layer to exercise FizzBuzz class
    '''
    cut = FizzBuzz()
    for number in range(1, 101):
        print(f'{number} => {cut.translate1(number)}')

    for number in range(1, 101):
        print(f'{number} => {cut.translate2(number)}')

    for number in range(1, 101):
        print(f'{number} => {cut.translate3(number)}')

def profile():
    '''
    Thin layer to exercise FizzBuzz class
    '''
    cut = FizzBuzz()
    for dummy in range(0,10000):
        for number in range(1, 101):
            cut.translate1(number)

        for number in range(1, 101):
            cut.translate2(number)

        for number in range(1, 101):
            cut.translate3(number)

if __name__ == "__main__":
    main()
    cProfile.run('profile()')
