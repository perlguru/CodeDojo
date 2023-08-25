'''
MineSweeper kata app
'''

from minesweeper.minesweeper import MineSweeper

def main():
    '''
    Thin layer to exercise MineSweeper class
    '''
    cut = MineSweeper()
    cut.set_board(cut.readfile("tests\\data\\board1.ms"))
    print("Initial")
    for row in cut.board:
        for col in row:
            print(col, end = '')
        print()

    cut.calculate()

    print()
    print("Solved")
    cut.print_solved()

if __name__ == "__main__":
    main()
