#!/usr/bin/env python

import unittest
from recipe5 import *

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite1 = loader.loadTestsFromTestCase(RomanNumeralConverterTest)
    suite2 = loader.loadTestsFromTestCase(RomanNumeralComboTest)

    suite = unittest.TestSuite([suite1, suite2])
    unittest.TextTestRunner(verbosity=2).run(suite)
