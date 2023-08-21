'''
Greed kata application
'''

from greed.greed import Greed

def main():
    '''
    Thin layer to exercise Greed class
    '''
    for roll in range(1,101):
        cut = Greed()
        cut.roll_dice(6)
        print (roll, cut.dice.tolist(), cut.score())


if __name__ == "__main__":
    main()
