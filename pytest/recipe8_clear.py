#!/usr/bin/env python

import unittest
from recipe8 import *

class RomanNumeralTest(unittest.TestCase):
    def setUp(self):
        self.cvt = RomanNumeralConverter()

    def test_convert_to_decimal_1(self):
        self.assertEquals(0, self.cvt.convert_to_decimal(""))

    def test_convert_to_decimal_2(self):
        self.assertEquals(1, self.cvt.convert_to_decimal("I"))

    def test_convert_to_decimal_3(self):
        self.assertEquals(2010, self.cvt.convert_to_decimal("MMX"))

    def test_convert_to_decimal_4(self):
        self.assertEquals(4000, self.cvt.convert_to_decimal("MMMM"))

    def test_convert_to_roman_1(self):
        self.assertEquals("", self.cvt.convert_to_roman(0))

    def test_convert_to_roman_2(self):
        self.assertEquals("II", self.cvt.convert_to_roman(2))

    def test_convert_to_roman_3(self):
        self.assertEquals("V", self.cvt.convert_to_roman(5))

    def test_convert_to_roman_4(self):
        self.assertEquals("XII", self.cvt.convert_to_roman(12))

    def test_convert_to_roman_5(self):
        self.assertEquals("MMX", self.cvt.convert_to_roman(2010))

    def test_convert_to_roman_6(self):
        self.assertEquals("MMMM", self.cvt.convert_to_roman(4000))

if __name__ == '__main__':
    unittest.main()
