import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_301(self):
        input = r""" """
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    def test_302(self):
        input = r"""
Var: a, b;
Var: c;

Function: foo
    Body:
    EndBody.

Function: main
    Body:
    EndBody.
"""
        expect = Program([
            VarDecl(Id("a"), [], None),
            VarDecl(Id("b"), [], None),
            VarDecl(Id("c"), [], None),
            FuncDecl(Id("foo"), [], ([], [])),
            FuncDecl(Id("main"), [], ([], []))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 302))
    def test_303(self):
        input = r"""
Var: a;
"""
        expect = Program([VarDecl(Id("a"), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    def test_304(self):
        input = r"""
Var: a1;
Var: b1, b2;
Var: c1, c2, c3;
"""
        expect = Program([
            VarDecl(Id("a1"), [], None),
            VarDecl(Id("b1"), [], None),
            VarDecl(Id("b2"), [], None),
            VarDecl(Id("c1"), [], None),
            VarDecl(Id("c2"), [], None),
            VarDecl(Id("c3"), [], None)
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    def test_305(self):
        input = r"""
Var: a1[0];
Var: a1[1], a2[1][2], a3[1][2][3], a4[1][2][3][4];
"""
        expect = Program([
            VarDecl(Id("a1"), [0], None),
            VarDecl(Id("a1"), [1], None),
            VarDecl(Id("a2"), [1, 2], None),
            VarDecl(Id("a3"), [1, 2, 3], None),
            VarDecl(Id("a4"), [1, 2, 3, 4], None)
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    def test_306(self):
        input = r"""
Var: a1[0o1][0o2][0o3][0o4][0o5][0o6][0o7];
Var: a1[0O1][0O2][0O3][0O4][0O5][0O6][0O7];
Var: a1[0o1000000000], a1[0O76543210];
"""
        expect = Program([
            VarDecl(Id("a1"), [1, 2, 3, 4, 5, 6, 7], None),
            VarDecl(Id("a1"), [1, 2, 3, 4, 5, 6, 7], None),
            VarDecl(Id("a1"), [134217728], None),
            VarDecl(Id("a1"), [16434824], None)
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 306))

    def test_307(self):
        input = r"""
Var: a[0x1][0x2][0x3][0x4][0x5][0x6][0x7][0x8][0x9];
Var: b[0xA][0xB][0xC][0xD][0xE][0xF];
Var: c[0X1][0X2][0X3][0X4][0X5][0X6][0X7][0X8][0X9];
Var: d[0XA][0XB][0XC][0XD][0XE][0XF];
Var: c[0x10000000], d[0XABCDEF];
Var: e[0x1234], e[0X8765];
"""
        expect = Program([
            VarDecl(Id("a"), [1, 2, 3, 4, 5, 6, 7, 8, 9], None),
            VarDecl(Id("b"), [10, 11, 12, 13, 14, 15], None),
            VarDecl(Id("c"), [1, 2, 3, 4, 5, 6, 7, 8, 9], None),
            VarDecl(Id("d"), [10, 11, 12, 13, 14, 15], None),
            VarDecl(Id("c"), [268435456], None),
            VarDecl(Id("d"), [11259375], None),
            VarDecl(Id("e"), [4660], None),
            VarDecl(Id("e"), [34661], None)
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 307))

    def test_308(self):
        input = r"""
Var: a = 1;
Var: a[1][2] = {1, 2};
"""
        expect = Program([
            VarDecl(Id("a"), [], IntLiteral(1)),
            VarDecl(Id("a"), [1, 2], ArrayLiteral(
                [IntLiteral(1), IntLiteral(2)]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    """ Function declaration """

    def test_309(self):
        input = r"""
Function: main
    Body:
    EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 309))

    def test_310(self):
        input = r"""
Function: main
    Body:
        Var: a;
    EndBody.
"""
        expect = Program(
            [FuncDecl(Id("main"), [], ([VarDecl(Id("a"), [], None)], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    def test_311(self):
        input = r"""
Function: main
    Body:
        foo();
    EndBody.
"""
        expect = Program(
            [FuncDecl(Id("main"), [], ([], [CallStmt(Id("foo"), [])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))

    def test_312(self):
        input = r"""
Function: main
    Body:
        Var: a;
        Var: b;
        foo1();
        foo2();
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([
                VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None)
            ], [CallStmt(Id("foo1"), []), CallStmt(Id("foo2"), [])]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))

    def test_313(self):
        input = r"""
Function: main
    Parameter: a
    Body:
    EndBody.
"""
        expect = Program(
            [FuncDecl(Id("main"), [VarDecl(Id("a"), [], None)], ([], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))

    def test_314(self):
        input = r"""
Function: main
    Parameter: a, b, c
    Body:
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [
                VarDecl(Id("a"), [], None),
                VarDecl(Id("b"), [], None),
                VarDecl(Id("c"), [], None)
            ], ([], []))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))
    def test_315(self):
        input = r"""
Function: main
    Parameter: a[0], b[123], c[0xABCDEF][0X123], d[0o7654][0O3210]
    Body:
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [
                VarDecl(Id("a"), [0], None),
                VarDecl(Id("b"), [123], None),
                VarDecl(Id("c"), [11259375, 291], None),
                VarDecl(Id("d"), [4012, 1672], None)
            ], ([], []))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))
    def test_316(self):
        input = r"""
Function: main
    Body:
        If True Then
        EndIf.
    EndBody.
"""
        expect = Program(
            [FuncDecl(Id("main"), [], ([], [If([(BooleanLiteral(True), [], [])], ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))
    def test_317(self):
        input = r"""
Function: main
    Body:
        If a Then
            Var: a;
        EndIf.
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [],
                     ([], [If([(Id("a"), [VarDecl(Id("a"), [], None)], [])], ([], []))]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 317))