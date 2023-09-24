"""
Test for MineSweeper kata.
"""

from minesweeper.minesweeper import MineSweeper, Board

BOARD1_SOLVED = '\
*100\n\
2210\n\
1*10\n\
1110\n'

class TestBoard:
    """
    Simple class to bundle our test under.
    """

    def test_create(self):
        """
        Intent:
        As a matter of style, always test that the class under test can create an
        object.
        """
        cut = Board()
        assert cut.rows == 8
        assert cut.columns == 8
        assert isinstance(cut, Board)
        cut = Board(4, 4)
        assert cut.rows == 4
        assert cut.columns == 4
        assert isinstance(cut, Board)

    def test_set_board(self):
        """
        Test that we can generate a 2d representation of the board
        """
        cut = Board()
        cut.set_board(cut.readfile("tests\\data\\board1.ms"))

        assert cut.rows == 4
        assert cut.columns == 4
        assert cut.columns == 4
        assert cut.board ==  [['*', '.', '.', '.'],
                              ['.', '.', '.', '.'],
                              ['.', '*', '.', '.'],
                              ['.', '.', '.', '.']]

    def test_readfile(self):
        """
        Just need to read the file
        """
        cut = Board()
        lines = cut.readfile("tests\\data\\board1.ms")
        assert lines == ['4 4', '*...', '....', '.*..', '....']

    class TestMineSweeper:
        """
        Simple class to bundle our test under.
        """

        def test_create(self):
            """
            Intent:
            As a matter of style, always test that the class under test can create an
            object.
            """
            cut = MineSweeper()
            assert isinstance(cut, MineSweeper)
            assert cut.board.rows == 8
            assert cut.board.columns == 8
            assert isinstance(cut.board, Board)
            assert not cut.solved

        def test_calculate(self):
            """
            Test that we can solve a simple puzzle
            """
            cut = Board()
            cut.set_board(cut.readfile("tests\\data\\board1.ms"))
            cut.calculate()
            assert cut.solved.board == [['*',  1,   0,   0],
                                        [ 2,   2,   1,   0],
                                        [ 1, '*',   1,   0],
                                        [ 1,   1,   1,   0]]

        def test_print_solved(self, capsys):
            """
            Not that interesting, but included for completeness.
            """
            cut = Board()
            cut.set_board(cut.readfile("tests\\data\\board1.ms"))
            cut.calculate()
#            cut.solved.display()
            cut.print_solved()
            captured = capsys.readouterr()
            assert captured.out == BOARD1_SOLVED

        def test_gen_board(self):
            cut = MineSweeper()
            cut.gen_board()
            assert isinstance(cut.board, Board)
