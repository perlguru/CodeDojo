'''
Hello World kata app
'''
import cProfile
from leapyear.leapyear import LeapYear

def main():
    '''
    Thin layer to exercise LeapYear class, and profile the 2 methods

    A lot of iterations are needed to detect observable difference.

    My results show that my leapyear1 is slightly faster than leapyear2

       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     25010000    4.942    0.000    4.942    0.000 leapyear.py:12(__init__)
     25010000   17.528    0.000   17.528    0.000 leapyear.py:18(leapyear1)
     25010000   17.836    0.000   17.836    0.000 leapyear.py:42(leapyear2)
    '''
    for dummy in range(0,10000):
        for testdate in range(1500,4001):
            dut = LeapYear(testdate)
            dut.leapyear1()
            dut.leapyear2()

if __name__ == "__main__":
    cProfile.run('main()')
