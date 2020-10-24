import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):

    def test_301(self):
        input = r"""
Var: x;
"""
        expect = Program([VarDecl(Id("x"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    def test_302(self):
        input = r"""
Var: a[1];
"""
        expect = Program([VarDecl(Id("a"),[None],None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 302))

    def test_303(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    def test_304(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    def test_305(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    def test_306(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 306))

    def test_307(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 307))

    def test_308(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    def test_309(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 309))

    def test_310(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    def test_311(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))

    def test_312(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))

    def test_313(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))

    def test_314(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))

    def test_315(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))

    def test_316(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))

    def test_317(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 317))

    def test_318(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))

    def test_319(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))

    def test_320(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))

    def test_321(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))

    def test_322(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 322))

    def test_323(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 323))

    def test_324(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 324))

    def test_325(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    def test_326(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    def test_327(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 327))

    def test_328(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 328))

    def test_329(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))

    def test_330(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 330))

    def test_331(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))

    def test_332(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))

    def test_333(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 333))

    def test_334(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))

    def test_335(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))

    def test_336(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 336))

    def test_337(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 337))

    def test_338(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 338))

    def test_339(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 339))

    def test_340(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 340))

    def test_341(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 341))

    def test_342(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 342))

    def test_343(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 343))

    def test_344(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 344))

    def test_345(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 345))

    def test_346(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 346))

    def test_347(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 347))

    def test_348(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 348))

    def test_349(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 349))

    def test_350(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 350))

    def test_351(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))

    def test_352(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))

    def test_353(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 353))

    def test_354(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 354))

    def test_355(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 355))

    def test_356(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))

    def test_357(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 357))

    def test_358(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))

    def test_359(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))

    def test_360(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))

    def test_361(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 361))

    def test_362(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 362))

    def test_363(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))

    def test_364(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 364))

    def test_365(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 365))

    def test_366(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))

    def test_367(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))

    def test_368(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))

    def test_369(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))

    def test_370(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))

    def test_371(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))

    def test_372(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))

    def test_373(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))

    def test_374(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))

    def test_375(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))

    def test_376(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))

    def test_377(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))

    def test_378(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))

    def test_379(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))

    def test_380(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 380))

    def test_381(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))

    def test_382(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))

    def test_383(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 383))

    def test_384(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 384))

    def test_385(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))

    def test_386(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))

    def test_387(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))

    def test_388(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 388))

    def test_389(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 389))

    def test_390(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 390))

    def test_391(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 391))

    def test_392(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 392))

    def test_393(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 393))

    def test_394(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 394))

    def test_395(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 395))

    def test_396(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 396))

    def test_397(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 397))

    def test_398(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 398))

    def test_399(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 399))

    def test_400(self):
        input = r"""

"""
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 400))
