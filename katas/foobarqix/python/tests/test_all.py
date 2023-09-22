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

    def test_translate1(self):
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
        assert cut.translate1(1) == '1'
        assert cut.translate1(3) == 'FooFoo'
        assert cut.translate1(5) == 'BarBar'
        assert cut.translate1(7) == 'QixQix'
        assert cut.translate1(15) == 'FooBarBar'
        assert cut.translate1(21) == 'FooQix'
        assert cut.translate1(33) == 'FooFooFoo'
        assert cut.translate1(35) == 'BarQixFooBar'
        assert cut.translate1(53) == 'BarFoo'
        assert cut.translate1(105) == 'FooBarQixBar'
        assert cut.translate1(30) == 'FooBarFoo'
        assert cut.translate1(50) == 'BarBar'
        assert cut.translate1(70) == 'BarQixQix'

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

    def test_translate3(self):
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
        assert cut.translate3(1) == '1'
        assert cut.translate3(3) == 'FooFoo'
        assert cut.translate3(5) == 'BarBar'
        assert cut.translate3(7) == 'QixQix'
        assert cut.translate3(15) == 'FooBarBar'
        assert cut.translate3(21) == 'FooQix'
        assert cut.translate3(33) == 'FooFooFoo'
        assert cut.translate3(35) == 'BarQixFooBar'
        assert cut.translate3(53) == 'BarFoo'
        assert cut.translate3(105) == 'FooBarQixBar'
        assert cut.translate3(30) == 'FooBarFoo'
        assert cut.translate3(50) == 'BarBar'
        assert cut.translate3(70) == 'BarQixQix'
