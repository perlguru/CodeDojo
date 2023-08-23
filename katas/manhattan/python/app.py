'''
Hello World kata app
'''

from manhattan.manhattan import Manhattan, Point

def main():
    '''
    Thin layer to exercise Hello class
    '''
    manhattan = Manhattan()
    print(manhattan.distance(Point (1,1), Point(2,2)))

if __name__ == "__main__":
    main()
