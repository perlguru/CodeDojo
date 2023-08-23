'''
Test for Manhatten Distance kata.
'''
import pytest

from manhattan.manhattan import Manhattan, Point

class TestPoint:
    '''
    Simple class to bundle our test under.
        Intent:
        As a matter of style, always test that the class under test can create an 
        object.
    '''
    def test_create(self):
        '''
        Intent:
        As a matter of style, always test that the class under test can create an 
        object.
        '''
        cut = Point(1, 1)
        assert isinstance(cut, Point)

    def test_imumutable_private(self):
        '''
        Test (as best as we can) that:
            The class Point is immutable
            The class Point has no Getters, no Setters
            The class Point has no public properties (i.e. the internal state
            cannot be read from outside the class).
        '''
        cut = Point(1, 1)

        # Set
        with pytest.raises(AttributeError):
            # Demonstrates immutability, private variables
            # Of course we are going to get a pylint error, but that is what
            # we are testing
            # pylint: disable=protected-access, unused-private-member
            cut.__x = 2

        # Get
        with pytest.raises(AttributeError):
            # Demonstrates private variables
            # Of course we are going to get a pylint error, but that is what
            # we are testing
            # pylint: disable=protected-access
            assert cut.__x == 2

class TestManhattan:
    '''
    Simple class to bundle our test under.
    '''

    def test_create(self):
        '''
        Intent:
        As a matter of style, always test that the class under test can create an 
        object.
        '''
        cut = Manhattan()
        assert isinstance(cut, Manhattan)

    def test_distance1(self):
        '''
        Intent:
        Test the kata requirements
        '''
        cut = Manhattan()
        assert cut.distance(Point(1, 1), Point(2, 2)) == 2
        assert cut.distance(Point(1, 1), Point(3, 3)) == 4
        assert cut.distance(Point(4, 4), Point(1, 1)) == 6
