# coding=utf-8
"""
Test for FooBarQix kata
"""

from foobarqix.foobarqix import FooBarQix

class TestFooBarQix:
    """
    Simple class to bundle our test under.
    """

    def test_create(self):
        """
        Intent:
        As a matter of style, always test that the class under test can create
        an object.
        """
        cut = FooBarQix()
        assert isinstance(cut, FooBarQix)

    def test_translate(self):
        """
        Intent:
        Given any number we sholud be able to apply the FooBarQix rules to get
        a string representation.

        For any number print the number, unless:
        If the number is divisible by 3, write “Foo” instead of the number
        If the number is divisible by 5, add “Bar”
        If the number is divisible by 7, add “Qix”
        For each digit 3, 5, 7, add “Foo”, “Bar”, “Qix” in the digits order.

        These test should be easily verifable by inspection.
        """
        cut = FooBarQix()
        assert cut.translate(1) == '1'
        assert cut.translate(3) == 'FooFoo'
        assert cut.translate(5) == 'BarBar'
        assert cut.translate(7) == 'QixQix'
        assert cut.translate(15) == 'FooBarBar'
        assert cut.translate(21) == 'FooQix'
        assert cut.translate(33) == 'FooFooFoo'
        assert cut.translate(35) == 'BarQixFooBar'
        assert cut.translate(53) == 'BarFoo'
        assert cut.translate(105) == 'FooBarQixBar'
        assert cut.translate(30) == 'FooBarFoo'
        assert cut.translate(50) == 'BarBar'
        assert cut.translate(70) == 'BarQixQix'

    def test_translate2(self):
        """
        Intent:
        Given any number we sholud be able to apply the FooBarQix rules to get
        a string representation.

        As before, plus:

        101   => 1*1
        303   => FooFoo*Foo
        105   => FooBarQix*Bar
        10101 => FooQix**

        These test should be asily verifable by inspection.
        """
        cut = FooBarQix()
        print(f"test {cut.translate2(101)}")
        assert cut.translate2(101) == '1*1'
        assert cut.translate2(303) == 'FooFoo*Foo'
        assert cut.translate2(105) == 'FooBarQix*Bar'
        assert cut.translate2(10101) == 'FooQix**'
