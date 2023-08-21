'''
Test for Greed kata
'''
import pytest

from greed.greed import Greed

class TestGreed:
    '''
    Simple class to bundle our test under.
    '''

    def test_create(self):
        '''
        Intent:
        As a matter of style, always test that the class under test can create
        an object.
        '''
        cut = Greed()
        assert isinstance(cut, Greed)

    def test_borg(self):
        '''
        Test Borg-ify
        '''
        cut1 = Greed([1, 2])
        cut2 = Greed([3, 4])
        assert cut1.dice == cut2.dice
        assert cut1.dice.tolist() == [3, 4]
        assert cut2.dice.tolist() == [3, 4]

    def test_count(self):
        '''
        Simply test that the number of dice we initialize is reflected.

        Note: maximum of 6 die are allowed. 7 die should be an assertion error.
        '''
        cut = Greed([1, 2])
        assert cut.get_count() == 2
        cut = Greed([1, 2, 3, 4, 5,6])
        assert cut.get_count() == 6


    def test_count_fail(self):
        '''
        Maximum of 6 die are allowed. 7 die should be an assertion error.
        '''
        with pytest.raises(ValueError):
            cut = Greed([1, 2, 3, 4, 5, 6, 7])
            assert cut.get_count() == 0

    def test_set_dice(self):
        '''
        We should be able to set the value of all dice in a single call
        '''
        cut = Greed()
        cut.set_dice([1, 2])
        assert cut.get_count() == 2
        cut.set_dice([1, 2, 3, 4, 5, 6])
        assert cut.get_count() == 6

    def test_set_dice_fail(self):
        '''
        6 die are the max 7 should raise an error
        '''
        cut = Greed()
        with pytest.raises(ValueError):
            cut.set_dice([1, 2, 3, 4, 5, 6, 7])

    def test_score_1_and_5(self):
        '''
        A single 1 is worth 50 points and a single 5 is worth 100 points
        '''
        cut = Greed([1, 2])
        assert cut.score() == 50
        cut.set_dice([1, 2, 3])
        assert cut.score() == 50
        cut.set_dice([1, 2, 5])
        assert cut.score() == 150
        cut.set_dice([2, 5])
        assert cut.score() == 100

    def test_score_x_of_akind(self):
        '''
        3, 4, 5, 6 of a kind takes on a fairly complex rule set. See kata for
        more detail.
        '''
        cut = Greed([])
        cut.set_dice([2, 2, 2, 1])
        assert cut.score() == 250
        cut.set_dice([5, 5, 5])
        assert cut.score() == 500
        cut.set_dice([2, 2, 2, 5])
        assert cut.score() == 300
        cut.set_dice([2, 2, 2])
        assert cut.score() == 200
        cut.set_dice([2, 2, 2, 3, 3, 3])
        assert cut.score() == 500
        cut.set_dice([2, 2, 2, 2])
        assert cut.score() == 400
        cut.set_dice([2, 2, 2, 2, 2])
        assert cut.score() == 800
        cut.set_dice([2, 2, 2, 2, 2, 2])
        assert cut.score() == 1600

    def test_score_straight(self):
        '''
        A straight is farly simple. You must have each of the six possible die
        pip counts
        '''
        cut = Greed([])
        cut.set_dice([1, 2, 3])
        assert cut.score() == 50
        cut.set_dice([1, 2, 3, 4, 5, 6])
        assert cut.score() == 1200
        cut.set_dice([1, 2, 3, 6, 5, 4])
        assert cut.score() == 1200

    def test_roll(self):
        '''
        Briefly test rolling dice
        '''
        cut = Greed()
        cut.roll_dice(6)
        assert cut.get_count() == 6

    def test_random(self):
        '''
        Random test based on observation of application
        '''
        cut = Greed([])
        cut.set_dice([5, 5, 5, 4, 3, 3])
        assert cut.score() == 500
