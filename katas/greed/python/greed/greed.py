'''
The Greed kata written in object oriented fashion.
'''


from array import array
import random

# pylint: disable=too-few-public-methods
class Borg:
    '''
    Greed is essentially the Game. There is no need to have mutiple instances,
	so we could use the Borg (Singleton) design pattern, or simply us class
	variables and classmethods. To reduce typing, we have chosen the former.
    '''
    data = {}

    def __init__(self):
        self.__dict__ = self.data

class Greed(Borg):
    '''
    Main Greed class
    '''

    def __init__(self, dice=None):
        '''
        Borg-ify instance
        '''
        Borg.__init__(self)
        if dice is None:
            dice = []

        if len(dice) > 6:
            raise ValueError

        if dice is None:
            dice = []
        self.set_dice(array('h', dice))

    def get_count(self):
        '''
        Get number of dice
        '''
        return len(self.dice)

    def get_dice(self):
        '''
        Get dice
        '''
        return self.dice

    def set_dice(self, dice):
        '''
        Set dice and ensure we dont have too many
        '''
        if len(dice) > 6:
            raise ValueError

        self.dice = dice

    def roll_dice(self, count):
        '''
        Randomize a certain number of die
        '''
        if count > 6:
            raise ValueError

        # pylint: disable=unused-variable
        for die in range(0, count):
            self.dice.append(random.randint(1, 6))

    def score(self):
        '''
        Get score of dice. To practice Single-Responsibility, we have 
        segragated the classes of scoring to individual methods.
        '''
        score = self.check_straight()
        score += self.check_3_pairs()
        score += self.checkx_of_akind()
        score += self.check1() + self.check5()

        return score

    def check_straight(self):
        '''
        Check for a straight. If we find a straight remove all die.
        '''
        score = 0
        if sorted(self.dice) == [1, 2, 3, 4, 5, 6]:
            self.set_dice([])
            score = 1200
        return score

    def check_3_pairs(self):
        '''
        Check for 3 pairs. If we find 3 pairs remove all die.
        '''
        total = 0
        score = 0
        for pip in [1, 2, 3, 4, 5, 6]:
            count = self.dice.count(pip)
            if count == 2:
                total += 1
        if total == 3:
            self.set_dice([])
            score = 800

        return score

    def checkx_of_akind(self):
        '''
        Check for 6, 5, 4 or 3 of a kind. If we find any of these, remove 
        matching die. Use a base score and multipler look up table.
        '''
        base = [1000, 200, 300, 400, 500, 600]
        multi = [0, 0, 1, 2, 4, 8]

        score = 0
        # Must check from 6 down to 3 so that we find highest score
        for length in [6, 5, 4, 3]:
            for pip in [1, 2, 3, 4, 5, 6]:
                if self.dice.count(pip) == length:
                    score += base[pip - 1] * multi[length - 1]
                    # pylint: disable=unused-variable
                    for die in range(0, length):
                        self.dice.remove(pip)
        return score

    def check1(self):
        '''
        Check for a 1
        '''
        score = 0
        if self.dice.count(1):
            score = 50

        return score

    def check5(self):
        '''
        Check for a 5
        '''
        score = 0
        if self.dice.count(5):
            score = 100
        return score
