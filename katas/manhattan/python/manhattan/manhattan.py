'''
The classic Hello world written in object oriented fashion.
'''

from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    '''
    Simple dataclass to contain a Point
    '''
    __x: int
    __y: int

    def distance(self, ptb):
        '''
        Given a second point, determine the manhattan distance between the 2 
        points.
        '''
        # Disable protected-access warning, this is because of python mechanics
        # pylint: disable=protected-access
        return abs(self.__x - ptb.__x) + abs(self.__y - ptb.__y)

# pylint: disable=too-few-public-methods
class Manhattan():
    '''
    Very simple class to contain our implementation.
    '''

    def distance(self, pta, ptb):
        '''
        Get manhattan distance.
        '''
        return pta.distance(ptb)
