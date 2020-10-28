import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """a := b := 4"""
        expect = str(Program([VarDecl(IntType(),'a'),VarDecl(IntType(),'b')]))
        self.assertTrue(TestAST.checkASTGen(input,expect,300))
       