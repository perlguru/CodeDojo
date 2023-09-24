"""
MineSweeper kata app
"""

from minesweeper.minesweeper import MineSweeper

def main():
    """
    Thin layer to exercise MineSweeper class
    """
    cut = MineSweeper()
    cut.board.set_board(cut.board.readfile("tests\\data\\board1.ms"))
    print("Initial")
    cut.board.display()


    print()
    print("Solved")
    cut.board.calculate()
    cut.board.print_solved()

if __name__ == "__main__":
    main()
