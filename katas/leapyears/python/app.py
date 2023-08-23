'''
Hello World kata app
'''

from leapyear.leapyear import LeapYear

def main():
    '''
    Thin layer to exercise LeapYear class
    '''
    for testdate in range(1500,4001):
        testdate = LeapYear(testdate)
        print(testdate.year, testdate.leapyear1(), testdate.leapyear2())

if __name__ == "__main__":
    main()
