'''
FizzBuzz kata application
'''

from fizzbuzz.fizzbuzz import FizzBuzz

def main():
    '''
    Thin layer to exercise FizzBuzz class
    '''
    cut = FizzBuzz()
    for number in range(1, 101):
        print(f'{number} => {cut.translate(number)}')

    print('----------')

    for number in range(1, 101):
        print(f'{number} => {cut.translate2(number)}')

if __name__ == "__main__":
    main()
