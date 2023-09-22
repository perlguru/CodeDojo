"""
Test for Args kata.
"""

from args.args import Args

class TestArgs:
    """
    Simple class to bundle our test under.
    """

    def test_create(self):
        """
        Intent:
        As a matter of style, always test that the class under test can create an 
        object.
        """
        cut = Args()
        assert isinstance(cut, Args)
