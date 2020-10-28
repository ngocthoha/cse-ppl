import unittest
from TestUtils import TestChecker


class CheckSuite(unittest.TestCase):
    def test_401(self):
        input = r"""
Var: a, b;
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 401))
