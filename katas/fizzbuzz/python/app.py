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
    Thin layer to profile different FizzBuzz translations.

    A lot of iterations are needed to detect observable difference.

    My results show that my translate1 2x faster than translate3 and translate3
    5x faster than translate 2.

       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      1000000    0.456    0.000    0.456    0.000 fizzbuzz.py:15(translate1)
      1000000    1.426    0.000    5.063    0.000 fizzbuzz.py:36(translate2)
      1000000    0.624    0.000    1.061    0.000 fizzbuzz.py:71(translate3)
      1000000    0.437    0.000    0.437    0.000 fizzbuzz.py:75(<lambda>)
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
