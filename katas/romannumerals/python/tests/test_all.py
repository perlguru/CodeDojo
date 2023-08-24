'''
Test for Roman Numeral kata.
'''

from roman.roman import Roman

class TestRoman:
    '''
    Simple class to bundle our test under.
    '''

    def test_create(self):
        '''
        Intent:
        As a matter of style, always test that the class under test can create an 
        object.
        '''
        cut = Roman()
        assert isinstance(cut, Roman)

    def test_toroman_1to11(self):
        '''
        Test numbers from 1 to 11
        '''
        cut = Roman()
        assert cut.toroman(1) == "I"
        assert cut.toroman(2) == "II"
        assert cut.toroman(3) == "III"
        assert cut.toroman(4) == "IV"
        assert cut.toroman(5) == "V"
        assert cut.toroman(6) == "VI"
        assert cut.toroman(7) == "VII"
        assert cut.toroman(8) == "VIII"
        assert cut.toroman(9) == "IX"
        assert cut.toroman(10) == "X"
        assert cut.toroman(11) == "XI"

    def test_toroman_44to51(self):
        '''
        Test numbers around 50
        '''
        cut = Roman()
        assert cut.toroman(44) == "XLIV"
        assert cut.toroman(45) == "XLV"
        assert cut.toroman(46) == "XLVI"
        assert cut.toroman(49) == "XLIX"
        assert cut.toroman(50) == "L"
        assert cut.toroman(51) == "LI"

    def test_toroman_49to101(self):
        '''
        Test numbers around 100
        '''
        cut = Roman()
        assert cut.toroman(89) == "LXXXIX"
        assert cut.toroman(90) == "XC"
        assert cut.toroman(91) == "XCI"
        assert cut.toroman(94) == "XCIV"
        assert cut.toroman(95) == "XCV"
        assert cut.toroman(96) == "XCVI"
        assert cut.toroman(99) == "XCIX"
        assert cut.toroman(100) == "C"
        assert cut.toroman(101) == "CI"

    def test_toroman_489to501(self):
        '''
        Test numbers around 500
        '''
        cut = Roman()
        assert cut.toroman(489) == "CDLXXXIX"
        assert cut.toroman(490) == "CDXC"
        assert cut.toroman(491) == "CDXCI"
        assert cut.toroman(494) == "CDXCIV"
        assert cut.toroman(495) == "CDXCV"
        assert cut.toroman(496) == "CDXCVI"
        assert cut.toroman(499) == "CDXCIX"
        assert cut.toroman(500) == "D"
        assert cut.toroman(501) == "DI"

    def test_toroman_989to1001(self):
        '''
        Test number from 1 to 11
        '''
        cut = Roman()
        assert cut.toroman(989) == "CMLXXXIX"
        assert cut.toroman(990) == "CMXC"
        assert cut.toroman(991) == "CMXCI"
        assert cut.toroman(994) == "CMXCIV"
        assert cut.toroman(995) == "CMXCV"
        assert cut.toroman(996) == "CMXCVI"
        assert cut.toroman(999) == "CMXCIX"
        assert cut.toroman(1000) == "M"
        assert cut.toroman(1001) == "MI"

    def test_toroman_gt1001(self):
        '''
        Test larger numbers
        '''
        cut = Roman()
        assert cut.toroman(1989) == "MCMLXXXIX"
        assert cut.toroman(1990) == "MCMXC"
        assert cut.toroman(1991) == "MCMXCI"
        assert cut.toroman(1994) == "MCMXCIV"
        assert cut.toroman(1995) == "MCMXCV"
        assert cut.toroman(1996) == "MCMXCVI"
        assert cut.toroman(1999) == "MCMXCIX"
        assert cut.toroman(2000) == "MM"
        assert cut.toroman(2001) == "MMI"

    def test_todigits_1to11(self):
        '''
        Test numbers from 1 to 11
        '''
        cut = Roman()
        assert cut.todigits("I") == 1
        assert cut.todigits("II") == 2
        assert cut.todigits("III") == 3
        assert cut.todigits("IV") == 4
        assert cut.todigits("V") == 5
        assert cut.todigits("VI") == 6
        assert cut.todigits("VII") == 7
        assert cut.todigits("VIII") == 8
        assert cut.todigits("IX") == 9
        assert cut.todigits("X") == 10
        assert cut.todigits("XI") == 11

    def test_todigits_44to51(self):
        '''
        Test numbers around 50
        '''
        cut = Roman()
        assert cut.todigits("XLIV") == 44
        assert cut.todigits("XLV") == 45
        assert cut.todigits("XLVI") == 46
        assert cut.todigits("XLIX") == 49
        assert cut.todigits("L") == 50
        assert cut.todigits("LI") == 51

    def test_todigits_49to101(self):
        '''
        Test numbers around 100
        '''
        cut = Roman()
        assert cut.todigits("LXXXIX") == 89
        assert cut.todigits("XC") == 90
        assert cut.todigits("XCI") == 91
        assert cut.todigits("XCIV") == 94
        assert cut.todigits("XCV") == 95
        assert cut.todigits("XCVI") == 96
        assert cut.todigits("XCIX") == 99
        assert cut.todigits("C") == 100
        assert cut.todigits("CI") == 101

    def test_todigits_489to501(self):
        '''
        Test numbers around 500
        '''
        cut = Roman()
        assert cut.todigits("CDLXXXIX") == 489
        assert cut.todigits("CDXC") == 490
        assert cut.todigits("CDXCI") == 491
        assert cut.todigits("CDXCIV") == 494
        assert cut.todigits("CDXCV") == 495
        assert cut.todigits("CDXCVI") == 496
        assert cut.todigits("CDXCIX") == 499
        assert cut.todigits("D") == 500
        assert cut.todigits("DI") == 501

    def test_todigits_989to1001(self):
        '''
        Test number from 1 to 11
        '''
        cut = Roman()
        assert cut.todigits("CMLXXXIX") == 989
        assert cut.todigits("CMXC") == 990
        assert cut.todigits("CMXCI") == 991
        assert cut.todigits("CMXCIV") == 994
        assert cut.todigits("CMXCV") == 995
        assert cut.todigits("CMXCVI") == 996
        assert cut.todigits("CMXCIX") == 999
        assert cut.todigits("M") == 1000
        assert cut.todigits("MI") == 1001

    def test_todigits_gt1001(self):
        '''
        Test larger numbers
        '''
        cut = Roman()
        assert cut.todigits("MCMLXXXIX") == 1989
        assert cut.todigits("MCMXC") == 1990
        assert cut.todigits("MCMXCI") == 1991
        assert cut.todigits("MCMXCIV") == 1994
        assert cut.todigits("MCMXCV") == 1995
        assert cut.todigits("MCMXCVI") == 1996
        assert cut.todigits("MCMXCIX") == 1999
        assert cut.todigits("MM") == 2000
        assert cut.todigits("MMI") == 2001
