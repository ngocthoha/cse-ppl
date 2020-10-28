import unittest
from TestUtils import TestChecker


class CheckSuite(unittest.TestCase):
    def test_401(self):
        input = r"""
Var: a, a;
"""
        expect = r"""Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_402(self):
        input = r"""
Var: a;

Function: a
Body:
EndBody.
"""
        expect = r"""Redeclared Function: a"""
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_403(self):
        input = r"""
Var: a;

Function: b
Body:
EndBody.

Function: b
Body:
EndBody.
"""
        expect = r"""Redeclared Function: b"""
        self.assertTrue(TestChecker.test(input, expect, 403))
