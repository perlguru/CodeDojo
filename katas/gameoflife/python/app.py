'''
Game of Life kata app
'''
import os
from time import sleep
from life.life import Board

BOARD1 = os.getcwd() + "\\" + "tests\\data\\board1.gol"
BOARD2 = os.getcwd() + "\\" + "tests\\data\\board2.gol"

def main():
    '''
    Thin layer to exercise Life class
    '''
    run_board(BOARD1)
    run_board(BOARD2)

def run_board(golboard):
    '''
    Runs a board for 20 generations
    '''
    os.system('clear')
    cut = Board()
    cut.load_from_file(golboard)
    cut.display()

    for dummy in range(0,20):
        cut = cut.compute_next()
        sleep(0.5)
        os.system('clear')
        cut.display()


if __name__ == "__main__":
    main()
