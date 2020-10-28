import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    """ Program structure """

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

    """ Variable declaration """

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

    """ If statement """

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

    def test_318(self):
        input = r"""
Function: main
    Body:
        If a Then
            foo();
        EndIf.
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [],
                     ([], [If([(Id("a"), [], [CallStmt(Id("foo"), [])])], ([], []))]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))

    def test_319(self):
        input = r"""
Function: main
    Body:
        If a Then
            Var: a, b;
            foo1();
            foo2();
        EndIf.
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                If([(Id("a"), [VarDecl(Id("a"), [], None),
                               VarDecl(Id("b"), [], None)],
                     [CallStmt(Id("foo1"), []), CallStmt(Id("foo2"), [])])], ([], []))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))

    def test_320(self):
        input = r"""
Function: main
    Body:
        If True Then
        ElseIf True Then
        EndIf.
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                If([(BooleanLiteral(True), [], []),
                    (BooleanLiteral(True), [], [])], ([], []))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))

    def test_321(self):
        input = r"""
Function: main
    Body:
        If True Then
        ElseIf True Then
        ElseIf True Then
        EndIf.
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                If([(BooleanLiteral(True), [], []), (BooleanLiteral(True), [], []),
                    (BooleanLiteral(True), [], [])], ([], []))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))

    def test_322(self):
        input = r"""
Function: main
    Body:
        If True Then
        ElseIf True Then
        ElseIf True Then
        ElseIf True Then
        ElseIf True Then
        ElseIf True Then
        EndIf.
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                If([(BooleanLiteral(True), [], []), (BooleanLiteral(True), [], []),
                    (BooleanLiteral(True), [], []), (BooleanLiteral(True), [], []),
                    (BooleanLiteral(True), [], []), (BooleanLiteral(True), [], [])], ([], []))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 322))

    def test_323(self):
        input = r"""
Function: main
    Body:
        If True Then
        ElseIf True Then
            Var: a;
        EndIf.
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                If([(BooleanLiteral(True), [], []),
                    (BooleanLiteral(True), [VarDecl(Id("a"), [], None)], [])], ([], []))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 323))

    def test_324(self):
        input = r"""
Function: main
    Body:
        If True Then
        ElseIf True Then
            foo();
        EndIf.
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                If([(BooleanLiteral(True), [], []),
                    (BooleanLiteral(True), [], [CallStmt(Id("foo"), [])])], ([], []))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 324))

    def test_325(self):
        input = r"""
Function: main
    Body:
        If True Then
        ElseIf True Then
            Var: a, b;
            foo1();
            foo2();
        EndIf.
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                If([(BooleanLiteral(True), [], []),
                    (BooleanLiteral(True), [VarDecl(Id("a"), [], None),
                                            VarDecl(Id("b"), [], None)],
                     [CallStmt(Id("foo1"), []), CallStmt(Id("foo2"), [])])], ([], []))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    def test_326(self):
        input = r"""
Function: main
    Body:
        If True Then
        ElseIf True Then
        Else
        EndIf.
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                If([(BooleanLiteral(True), [], []),
                    (BooleanLiteral(True), [], [])], ([], []))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    def test_327(self):
        input = r"""
Function: main
    Body:
        If True Then
        Else
        EndIf.
    EndBody.
"""
        expect = Program(
            [FuncDecl(Id("main"), [], ([], [If([(BooleanLiteral(True), [], [])], ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 327))

    def test_328(self):
        input = r"""
Function: main
    Body:
        If True Then
        Else
            Var: a;
        EndIf.
    EndBody.
"""
        expect = Program([
            FuncDecl(
                Id("main"), [],
                ([], [If([(BooleanLiteral(True), [], [])], ([VarDecl(Id("a"), [], None)], []))]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 328))

    def test_329(self):
        input = r"""
Function: main
    Body:
        If True Then
        Else
            foo();
        EndIf.
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [],
                     ([], [If([(BooleanLiteral(True), [], [])], ([], [CallStmt(Id("foo"), [])]))]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))

    def test_330(self):
        input = r"""
Function: main
    Body:
        If True Then
        Else
            Var: a, b;
            foo1();
            foo2();
        EndIf.
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                If([(BooleanLiteral(True), [], [])],
                   ([VarDecl(Id("a"), [], None),
                     VarDecl(Id("b"), [], None)],
                    [CallStmt(Id("foo1"), []), CallStmt(Id("foo2"), [])]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 330))

    """ While """

    def test_331(self):
        input = r"""
Function: main
    Body:
        While True Do
        EndWhile.
    EndBody.
"""
        expect = Program(
            [FuncDecl(Id("main"), [], ([], [While(BooleanLiteral(True), ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))

    def test_332(self):
        input = r"""
Function: main
    Body:
        While True Do
            Var: a;
        EndWhile.
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [],
                     ([], [While(BooleanLiteral(True), ([VarDecl(Id("a"), [], None)], []))]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))

    def test_333(self):
        input = r"""
Function: main
    Body:
        While True Do
            foo();
        EndWhile.
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [],
                     ([], [While(BooleanLiteral(True), ([], [CallStmt(Id("foo"), [])]))]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 333))

    def test_334(self):
        input = r"""
Function: main
    Body:
        While True Do
            Var: a, b;
            foo1();
            foo2();
        EndWhile.
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                While(
                    BooleanLiteral(True),
                    ([VarDecl(Id("a"), [], None),
                      VarDecl(Id("b"), [], None)],
                     [CallStmt(Id("foo1"), []), CallStmt(Id("foo2"), [])]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))

    """ Do while """

    def test_335(self):
        input = r"""
Function: main
    Body:
        Do
        While True
        EndDo.
    EndBody.
"""
        expect = Program(
            [FuncDecl(Id("main"), [], ([], [Dowhile(([], []), BooleanLiteral(True))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))

    def test_336(self):
        input = r"""
Function: main
    Body:
        Do
            Var: a;
        While True
        EndDo.
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [],
                     ([], [Dowhile(([VarDecl(Id("a"), [], None)], []), BooleanLiteral(True))]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 336))

    def test_337(self):
        input = r"""
Function: main
    Body:
        Do
            foo();
        While True
        EndDo.
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [],
                     ([], [Dowhile(([], [CallStmt(Id("foo"), [])]), BooleanLiteral(True))]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 337))

    def test_338(self):
        input = r"""
Function: main
    Body:
        Do
            Var: a, b;
            foo1();
            foo2();
        While True
        EndDo.
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Dowhile(
                    ([VarDecl(Id("a"), [], None),
                      VarDecl(Id("b"), [], None)],
                     [CallStmt(Id("foo1"), []), CallStmt(Id("foo2"), [])]), BooleanLiteral(True))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 338))

    """ Break """

    def test_339(self):
        input = r"""
Function: main
    Body:
        Break;
    EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [Break()]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 339))

    def test_340(self):
        input = r"""
Function: main
    Body:
        Continue;
    EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [Continue()]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 340))

    def test_341(self):
        input = r"""
Function: main
    Body:
        Return 1;
    EndBody.
"""
        expect = Program(
            [FuncDecl(Id("main"), [], ([], [Return(IntLiteral(1))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 341))

    def test_342(self):
        input = r"""
Function: main
    Body:
        Return;
    EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 342))

    """ Funccall """

    def test_343(self):
        input = r"""
Function: main
    Body:
        foo(a);
    EndBody.
"""
        expect = Program(
            [FuncDecl(Id("main"), [], ([], [CallStmt(Id("foo"), [Id("a")])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 343))

    def test_344(self):
        input = r"""
Function: main
    Body:
        foo(1, a[2], True, "", 1.);
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                CallStmt(Id("foo"), [
                    IntLiteral(1),
                    ArrayCell(Id("a"), [IntLiteral(2)]),
                    BooleanLiteral(True),
                    StringLiteral(""),
                    FloatLiteral(1.0)
                ])
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 344))
    def test_345(self):
        input = r"""
Function: main
    Body:
        foo(foo(foo()));
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [],
                     ([], [CallStmt(Id("foo"), [CallExpr(Id("foo"), [CallExpr(Id("foo"), [])])])]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 345))

    """ Assignment """

    def test_346(self):
        input = r"""
Function: main
    Body:
        a = 1;
    EndBody.
"""
        expect = Program(
            [FuncDecl(Id("main"), [], ([], [Assign(Id("a"), IntLiteral(1))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 346))

    def test_347(self):
        input = r"""
Function: main
    Body:
        a[1] = 1;
        a[-1][foo() + a] = 1;
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(ArrayCell(Id("a"), [IntLiteral(1)]), IntLiteral(1)),
                Assign(
                    ArrayCell(Id("a"), [
                        UnaryOp("-", IntLiteral(1)),
                        BinaryOp("+", CallExpr(Id("foo"), []), Id("a"))
                    ]), IntLiteral(1))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 347))

    def test_348(self):
        input = r"""
Function: main
    Body:
        a = 1;
        a = 1.0;
        a = True;
        a = False;
        a = "Hello World \n";
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(Id("a"), IntLiteral(1)),
                Assign(Id("a"), FloatLiteral(1.0)),
                Assign(Id("a"), BooleanLiteral(True)),
                Assign(Id("a"), BooleanLiteral(False)),
                Assign(Id("a"), StringLiteral(r"""Hello World \n"""))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 348))

    def test_349(self):
        input = r"""
Function: main
    Body:
        foo(0o1,0o2,0o3,0o4,0o5,0o6,0o7);
        foo(0O1,0O2,0O3,0O4,0O5,0O6,0O7);
        foo(0o1000000000,0O76543210);
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                CallStmt(Id("foo"), [
                    IntLiteral(1),
                    IntLiteral(2),
                    IntLiteral(3),
                    IntLiteral(4),
                    IntLiteral(5),
                    IntLiteral(6),
                    IntLiteral(7)
                ]),
                CallStmt(Id("foo"), [
                    IntLiteral(1),
                    IntLiteral(2),
                    IntLiteral(3),
                    IntLiteral(4),
                    IntLiteral(5),
                    IntLiteral(6),
                    IntLiteral(7)
                ]),
                CallStmt(Id("foo"),
                         [IntLiteral(134217728), IntLiteral(16434824)])
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 349))

    def test_350(self):
        input = r"""
Function: main
    Body:
        foo(0x1,0x2,0x3,0x4,0x5,0x6,0x7,0x8,0x9);
        foo(0xA,0xB,0xC,0xD,0xE,0xF);
        foo(0X1,0X2,0X3,0X4,0X5,0X6,0X7,0X8,0X9);
        foo(0XA,0XB,0XC,0XD,0XE,0XF);
        foo(0x10000000,0XABCDEF);
        foo(0x1234,0X8765);
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                CallStmt(Id("foo"), [
                    IntLiteral(1),
                    IntLiteral(2),
                    IntLiteral(3),
                    IntLiteral(4),
                    IntLiteral(5),
                    IntLiteral(6),
                    IntLiteral(7),
                    IntLiteral(8),
                    IntLiteral(9)
                ]),
                CallStmt(Id("foo"), [
                    IntLiteral(10),
                    IntLiteral(11),
                    IntLiteral(12),
                    IntLiteral(13),
                    IntLiteral(14),
                    IntLiteral(15)
                ]),
                CallStmt(Id("foo"), [
                    IntLiteral(1),
                    IntLiteral(2),
                    IntLiteral(3),
                    IntLiteral(4),
                    IntLiteral(5),
                    IntLiteral(6),
                    IntLiteral(7),
                    IntLiteral(8),
                    IntLiteral(9)
                ]),
                CallStmt(Id("foo"), [
                    IntLiteral(10),
                    IntLiteral(11),
                    IntLiteral(12),
                    IntLiteral(13),
                    IntLiteral(14),
                    IntLiteral(15)
                ]),
                CallStmt(Id("foo"),
                         [IntLiteral(268435456), IntLiteral(11259375)]),
                CallStmt(Id("foo"), [IntLiteral(4660), IntLiteral(34661)])
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 350))
        
    def test_351(self):
        input = r"""
Function: main
    Body:
        a = True;
        a = False;
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(Id("a"), BooleanLiteral(True)),
                Assign(Id("a"), BooleanLiteral(False))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))

    def test_352(self):
        input = r"""
Function: main
    Body:
        a = "abcd";
    EndBody.
"""
        expect = Program(
            [FuncDecl(Id("main"), [], ([], [Assign(Id("a"), StringLiteral(r"""abcd"""))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))

    def test_353(self):
        input = r"""
Function: main
    Body:
        a = { 1, 2, 3, 4 };
        a = { 1.0, 2.0, 3.0, 4.0 };
        a = { True, False };
        a = { {1,2}, {3,4} };
        a = {{{{{1}}}}};
        a = {{{{{1}}}}, {1}, 1};
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(Id("a"),
                       ArrayLiteral([IntLiteral(1),
                                     IntLiteral(2),
                                     IntLiteral(3),
                                     IntLiteral(4)])),
                Assign(
                    Id("a"),
                    ArrayLiteral([
                        FloatLiteral(1.0),
                        FloatLiteral(2.0),
                        FloatLiteral(3.0),
                        FloatLiteral(4.0)
                    ])),
                Assign(Id("a"), ArrayLiteral([BooleanLiteral(True),
                                              BooleanLiteral(False)])),
                Assign(
                    Id("a"),
                    ArrayLiteral([
                        ArrayLiteral([IntLiteral(1), IntLiteral(2)]),
                        ArrayLiteral([IntLiteral(3), IntLiteral(4)])
                    ])),
                Assign(
                    Id("a"),
                    ArrayLiteral([
                        ArrayLiteral(
                            [ArrayLiteral([ArrayLiteral([ArrayLiteral([IntLiteral(1)])])])])
                    ])),
                Assign(
                    Id("a"),
                    ArrayLiteral([
                        ArrayLiteral(
                            [ArrayLiteral([ArrayLiteral([ArrayLiteral([IntLiteral(1)])])])]),
                        ArrayLiteral([IntLiteral(1)]),
                        IntLiteral(1)
                    ]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 353))

    def test_354(self):
        input = r"""
Function: main
    Body:
        a = abcd;
    EndBody.
"""
        expect = Program(
            [FuncDecl(Id("main"), [], ([], [Assign(Id("a"), Id("abcd"))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 354))

    def test_355(self):
        input = r"""
Function: main
    Body:
        a = (a);
    EndBody.
"""
        expect = Program(
            [FuncDecl(Id("main"), [], ([], [Assign(Id("a"), Id("a"))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 355))

    def test_356(self):
        input = r"""
Function: main
    Body:
        a = (((a)));
    EndBody.
"""
        expect = Program(
            [FuncDecl(Id("main"), [], ([], [Assign(Id("a"), Id("a"))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))

    def test_357(self):
        input = r"""
Function: main
    Body:
        a = foo();
        a = foo(1, True, "", 1.);
        a = foo(foo(foo()));
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(Id("a"), CallExpr(Id("foo"), [])),
                Assign(
                    Id("a"),
                    CallExpr(
                        Id("foo"),
                        [IntLiteral(1),
                         BooleanLiteral(True),
                         StringLiteral(""),
                         FloatLiteral(1.0)])),
                Assign(Id("a"), CallExpr(Id("foo"),
                                         [CallExpr(Id("foo"), [CallExpr(Id("foo"), [])])]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 357))

    def test_358(self):
        input = r"""
Function: main
    Body:
        a = a[-1][foo() + "abcd"];
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(
                    Id("a"),
                    ArrayCell(Id("a"), [
                        UnaryOp("-", IntLiteral(1)),
                        BinaryOp("+", CallExpr(Id("foo"), []),
                                 StringLiteral(r"""abcd"""))
                    ]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))
    def test_359(self):
        input = r"""
Function: main
    Body:
        a = 1 * 1;
        a = 1 *. 1;
        a = 1 \ 1;
        a = 1 \. 1;
        a = 1 % 1;
        a = 1 + 1;
        a = 1 +. 1;
        a = 1 - 1;
        a = 1 -. 1;
        a = 1 && 1;
        a = 1 || 1;
        a = 1 == 1;
        a = 1 != 1;
        a = 1 =/= 1;
        a = 1 < 1;
        a = 1 <. 1;
        a = 1 > 1;
        a = 1 >. 1;
        a = 1 <= 1;
        a = 1 <=. 1;
        a = 1 >= 1;
        a = 1 >=. 1;
        a = !1;
        a = -1;
        a = -.1;
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(Id("a"), BinaryOp("*", IntLiteral(1), IntLiteral(1))),
                Assign(Id("a"), BinaryOp("*.", IntLiteral(1), IntLiteral(1))),
                Assign(Id("a"), BinaryOp("\\", IntLiteral(1), IntLiteral(1))),
                Assign(Id("a"), BinaryOp("\\.", IntLiteral(1), IntLiteral(1))),
                Assign(Id("a"), BinaryOp("%", IntLiteral(1), IntLiteral(1))),
                Assign(Id("a"), BinaryOp("+", IntLiteral(1), IntLiteral(1))),
                Assign(Id("a"), BinaryOp("+.", IntLiteral(1), IntLiteral(1))),
                Assign(Id("a"), BinaryOp("-", IntLiteral(1), IntLiteral(1))),
                Assign(Id("a"), BinaryOp("-.", IntLiteral(1), IntLiteral(1))),
                Assign(Id("a"), BinaryOp("&&", IntLiteral(1), IntLiteral(1))),
                Assign(Id("a"), BinaryOp("||", IntLiteral(1), IntLiteral(1))),
                Assign(Id("a"), BinaryOp("==", IntLiteral(1), IntLiteral(1))),
                Assign(Id("a"), BinaryOp("!=", IntLiteral(1), IntLiteral(1))),
                Assign(Id("a"), BinaryOp("=/=", IntLiteral(1), IntLiteral(1))),
                Assign(Id("a"), BinaryOp("<", IntLiteral(1), IntLiteral(1))),
                Assign(Id("a"), BinaryOp("<.", IntLiteral(1), IntLiteral(1))),
                Assign(Id("a"), BinaryOp(">", IntLiteral(1), IntLiteral(1))),
                Assign(Id("a"), BinaryOp(">.", IntLiteral(1), IntLiteral(1))),
                Assign(Id("a"), BinaryOp("<=", IntLiteral(1), IntLiteral(1))),
                Assign(Id("a"), BinaryOp("<=.", IntLiteral(1), IntLiteral(1))),
                Assign(Id("a"), BinaryOp(">=", IntLiteral(1), IntLiteral(1))),
                Assign(Id("a"), BinaryOp(">=.", IntLiteral(1), IntLiteral(1))),
                Assign(Id("a"), UnaryOp("!", IntLiteral(1))),
                Assign(Id("a"), UnaryOp("-", IntLiteral(1))),
                Assign(Id("a"), UnaryOp("-.", IntLiteral(1)))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))

    def test_360(self):
        input = r"""
Function: main
    Body:
        a = 1 * 1 * 1;
        a = 1 *. 1 *. 1;
        a = 1 \ 1 \ 1;
        a = 1 \. 1 \. 1;
        a = 1 % 1 % 1;
        a = 1 + 1 + 1;
        a = 1 +. 1 +. 1;
        a = 1 - 1 - 1;
        a = 1 -. 1 -. 1;
        a = 1 && 1 && 1;
        a = 1 || 1 || 1;
        a = !!1;
        a = --1;
        a = -.-.1;
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(Id("a"),
                       BinaryOp("*", BinaryOp("*", IntLiteral(1), IntLiteral(1)), IntLiteral(1))),
                Assign(Id("a"),
                       BinaryOp("*.", BinaryOp("*.", IntLiteral(1), IntLiteral(1)), IntLiteral(1))),
                Assign(Id("a"),
                       BinaryOp("\\", BinaryOp("\\", IntLiteral(1), IntLiteral(1)), IntLiteral(1))),
                Assign(
                    Id("a"),
                    BinaryOp("\\.", BinaryOp("\\.", IntLiteral(1), IntLiteral(1)), IntLiteral(1))),
                Assign(Id("a"),
                       BinaryOp("%", BinaryOp("%", IntLiteral(1), IntLiteral(1)), IntLiteral(1))),
                Assign(Id("a"),
                       BinaryOp("+", BinaryOp("+", IntLiteral(1), IntLiteral(1)), IntLiteral(1))),
                Assign(Id("a"),
                       BinaryOp("+.", BinaryOp("+.", IntLiteral(1), IntLiteral(1)), IntLiteral(1))),
                Assign(Id("a"),
                       BinaryOp("-", BinaryOp("-", IntLiteral(1), IntLiteral(1)), IntLiteral(1))),
                Assign(Id("a"),
                       BinaryOp("-.", BinaryOp("-.", IntLiteral(1), IntLiteral(1)), IntLiteral(1))),
                Assign(Id("a"),
                       BinaryOp("&&", BinaryOp("&&", IntLiteral(1), IntLiteral(1)), IntLiteral(1))),
                Assign(Id("a"),
                       BinaryOp("||", BinaryOp("||", IntLiteral(1), IntLiteral(1)), IntLiteral(1))),
                Assign(Id("a"), UnaryOp("!", UnaryOp("!", IntLiteral(1)))),
                Assign(Id("a"), UnaryOp("-", UnaryOp("-", IntLiteral(1)))),
                Assign(Id("a"), UnaryOp("-.", UnaryOp("-.", IntLiteral(1))))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))

    def test_361(self):
        input = r"""
Function: main
    Body:
        a = (a < b) && (d >= d);
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(
                    Id("a"),
                    BinaryOp("&&", BinaryOp("<", Id("a"), Id("b")), BinaryOp(
                        ">=", Id("d"), Id("d"))))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 361))

    def test_362(self):
        input = r"""
Function: main
    Body:
        a = 1+-1;
    EndBody.
"""
        expect = Program([
            FuncDecl(
                Id("main"), [],
                ([], [Assign(Id("a"), BinaryOp("+", IntLiteral(1), UnaryOp("-", IntLiteral(1))))]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 362))

    def test_363(self):
        input = r"""
Function: main
    Body:
        a = !-1;
        a = !-.1;
        a = --.1;
        a = -.-1;
        a = !--1;
        a = !-.-.1;
        a = !--.1;
        a = !-.-1;
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(Id("a"), UnaryOp("!", UnaryOp("-", IntLiteral(1)))),
                Assign(Id("a"), UnaryOp("!", UnaryOp("-.", IntLiteral(1)))),
                Assign(Id("a"), UnaryOp("-", UnaryOp("-.", IntLiteral(1)))),
                Assign(Id("a"), UnaryOp("-.", UnaryOp("-", IntLiteral(1)))),
                Assign(Id("a"), UnaryOp("!", UnaryOp(
                    "-", UnaryOp("-", IntLiteral(1))))),
                Assign(Id("a"), UnaryOp("!", UnaryOp(
                    "-.", UnaryOp("-.", IntLiteral(1))))),
                Assign(Id("a"), UnaryOp("!", UnaryOp(
                    "-", UnaryOp("-.", IntLiteral(1))))),
                Assign(Id("a"), UnaryOp("!", UnaryOp(
                    "-.", UnaryOp("-", IntLiteral(1)))))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))

    def test_364(self):
        input = r"""
Function: main
    Body:
        a = !a[1] > b || c + foo() * -e[2][abcd] % a \ True;
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(
                    Id("a"),
                    BinaryOp(
                        ">", UnaryOp("!", ArrayCell(Id("a"), [IntLiteral(1)])),
                        BinaryOp(
                            "||", Id("b"),
                            BinaryOp(
                                "+", Id("c"),
                                BinaryOp(
                                    "\\",
                                    BinaryOp(
                                        "%",
                                        BinaryOp(
                                            "*", CallExpr(Id("foo"), []),
                                            UnaryOp("-",
                                                    ArrayCell(Id("e"), [IntLiteral(2),
                                                                        Id("abcd")]))), Id("a")),
                                    BooleanLiteral(True))))))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 364))

    def test_365(self):
        input = r"""
Var: a, b[1], c[1][1], d = 1, e = 1e1, f = "Hello", g = True, i = {{1,2}};

Function: main
    Parameter: a, a[1], a[1][1]
    Body:
        Var: a = 1, b = 1., c = "", d = True;
        Var: sum = 0;
        While a < 10 Do
            Var: b = 1, prod = 1;
            While b < 10 Do
                prod = prod * b;
                b = b + 1;
            EndWhile.
            sum = sum + prod;
            a = a + 1;
        EndWhile.
    EndBody.
"""
        expect = Program([
            VarDecl(Id("a"), [], None),
            VarDecl(Id("b"), [1], None),
            VarDecl(Id("c"), [1, 1], None),
            VarDecl(Id("d"), [], IntLiteral(1)),
            VarDecl(Id("e"), [], FloatLiteral(10.0)),
            VarDecl(Id("f"), [], StringLiteral(r"""Hello""")),
            VarDecl(Id("g"), [], BooleanLiteral(True)),
            VarDecl(Id("i"), [], ArrayLiteral([ArrayLiteral([IntLiteral(1),
                                                             IntLiteral(2)])])),
            FuncDecl(Id("main"), [
                VarDecl(Id("a"), [], None),
                VarDecl(Id("a"), [1], None),
                VarDecl(Id("a"), [1, 1], None)
            ], ([
                VarDecl(Id("a"), [], IntLiteral(1)),
                VarDecl(Id("b"), [], FloatLiteral(1.0)),
                VarDecl(Id("c"), [], StringLiteral("")),
                VarDecl(Id("d"), [], BooleanLiteral(True)),
                VarDecl(Id("sum"), [], IntLiteral(0))
            ], [
                While(
                    BinaryOp("<", Id("a"), IntLiteral(10)),
                    ([VarDecl(Id("b"), [], IntLiteral(1)),
                      VarDecl(Id("prod"), [], IntLiteral(1))], [
                          While(BinaryOp("<", Id("b"), IntLiteral(10)), ([], [
                              Assign(Id("prod"), BinaryOp(
                                  "*", Id("prod"), Id("b"))),
                              Assign(Id("b"), BinaryOp(
                                  "+", Id("b"), IntLiteral(1)))
                          ])),
                          Assign(Id("sum"), BinaryOp(
                              "+", Id("sum"), Id("prod"))),
                          Assign(Id("a"), BinaryOp(
                              "+", Id("a"), IntLiteral(1)))
                    ]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 365))

    