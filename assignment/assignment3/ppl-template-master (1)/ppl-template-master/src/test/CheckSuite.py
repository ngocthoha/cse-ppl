import unittest
from TestUtils import TestChecker


class CheckSuite(unittest.TestCase):
    """ Redeclared """
    def test_401(self):
        input = r"""
Var: a, a;
Function: main
Body:
EndBody.
"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_402(self):
        input = r"""
Var: a;

Function: a
Body:
EndBody.

Function: main
Body:
EndBody.
"""
        expect = "Redeclared Function: a"
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

Function: main
Body:
EndBody.
"""
        expect = "Redeclared Function: b"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_404(self):
        input = r"""

Function: b
Parameter: a
Body:
    Var: a;
EndBody.

Function: main
Body:
EndBody.
"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_405(self):
        input = r"""
Var: print;
Function: main
Body:
EndBody.
"""
        expect = "Redeclared Variable: print"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_406(self):
        input = r"""
Var: printLn;
Function: main
Body:
EndBody.
"""
        expect = "Redeclared Variable: printLn"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_407(self):
        input = r"""
Var: printStrLn;
Function: main
Body:
EndBody.
"""
        expect = "Redeclared Variable: printStrLn"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_408(self):
        input = r"""
Var: read;
Function: main
Body:
EndBody.
"""
        expect = "Redeclared Variable: read"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_409(self):
        input = r"""
Function: main
Parameter: a, a
Body:
EndBody.

"""
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_410(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_411(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_412(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_413(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_414(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_415(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_416(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_417(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_418(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_419(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_420(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_421(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_422(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_423(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_424(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_425(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_426(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_427(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_428(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_429(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_430(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_431(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_432(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_433(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_434(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_435(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_436(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_437(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_438(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_439(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_440(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_441(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_442(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_443(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_444(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_445(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_446(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_447(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_448(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_449(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_450(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_451(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_452(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_453(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_454(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_455(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_456(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_457(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_458(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_459(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_460(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_461(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_462(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_463(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_464(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_465(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_466(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_467(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_468(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_469(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_470(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_471(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_472(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_473(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_474(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_475(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_476(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_477(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_478(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_479(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_480(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_481(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_482(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_483(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_484(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_485(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_486(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_487(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_488(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_489(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_490(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_491(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_492(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_493(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_494(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_495(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_496(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_497(self):
        input = r"""
Function: main
Body:
EndBody.
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 497))
