import unittest
from TestUtils import TestCodeGen
from AST import *

class CheckCodeGenSuite(unittest.TestCase):
	def test_number_400(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(200.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 400))

	def test_number_401(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(201.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 401))

	def test_number_402(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(202.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 402))

	def test_number_403(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(203.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 403))

	def test_number_404(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(204.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 404))

	def test_number_405(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(205.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 405))

	def test_number_406(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(206.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 406))

	def test_number_407(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(207.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 407))

	def test_number_408(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(208.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 408))

	def test_number_409(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(209.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 409))

	def test_number_410(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(210.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 410))

	def test_number_411(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(211.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 411))

	def test_number_412(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(212.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 412))

	def test_number_413(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(213.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 413))

	def test_number_414(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(214.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 414))

	def test_number_415(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(215.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 415))

	def test_number_416(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(216.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 416))

	def test_number_417(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(217.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 417))

	def test_number_418(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(218.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 418))

	def test_number_419(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(219.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 419))

	def test_number_420(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(220.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 420))

	def test_number_421(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(221.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 421))

	def test_number_422(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(222.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 422))

	def test_number_423(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(223.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 423))

	def test_number_424(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(224.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 424))

	def test_number_425(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(225.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 425))

	def test_number_426(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(226.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 426))

	def test_number_427(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(227.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 427))

	def test_number_428(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(228.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 428))

	def test_number_429(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(229.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 429))

	def test_number_430(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(230.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 430))

	def test_number_431(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(231.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 431))

	def test_number_432(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(232.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 432))

	def test_number_433(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(233.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 433))

	def test_number_434(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(234.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 434))

	def test_number_435(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(235.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 435))

	def test_number_436(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(236.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 436))

	def test_number_437(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(237.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 437))

	def test_number_438(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(238.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 438))

	def test_number_439(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(239.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 439))

	def test_number_440(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(240.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 440))

	def test_number_441(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(241.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 441))

	def test_number_442(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(242.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 442))

	def test_number_443(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(243.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 443))

	def test_number_444(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(244.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 444))

	def test_number_445(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(245.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 445))

	def test_number_446(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(246.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 446))

	def test_number_447(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(247.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 447))

	def test_number_448(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(248.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 448))

	def test_number_449(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(249.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 449))

	def test_number_450(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(250.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 450))

	def test_number_451(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(251.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 451))

	def test_number_452(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(252.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 452))

	def test_number_453(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(253.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 453))

	def test_number_454(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(254.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 454))

	def test_number_455(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(255.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 455))

	def test_number_456(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(256.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 456))

	def test_number_457(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(257.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 457))

	def test_number_458(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(258.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 458))

	def test_number_459(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(259.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 459))

	def test_number_460(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(260.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 460))

	def test_number_461(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(261.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 461))

	def test_number_462(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(262.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 462))

	def test_number_463(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(263.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 463))

	def test_number_464(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(264.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 464))

	def test_number_465(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(265.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 465))

	def test_number_466(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(266.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 466))

	def test_number_467(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(267.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 467))

	def test_number_468(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(268.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 468))

	def test_number_469(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(269.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 469))

	def test_number_470(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(270.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 470))

	def test_number_471(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(271.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 471))

	def test_number_472(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(272.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 472))

	def test_number_473(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(273.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 473))

	def test_number_474(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(274.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 474))

	def test_number_475(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(275.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 475))

	def test_number_476(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(276.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 476))

	def test_number_477(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(277.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 477))

	def test_number_478(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(278.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 478))

	def test_number_479(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(279.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 479))

	def test_number_480(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(280.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 480))

	def test_number_481(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(281.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 481))

	def test_number_482(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(282.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 482))

	def test_number_483(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(283.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 483))

	def test_number_484(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(284.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 484))

	def test_number_485(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(285.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 485))

	def test_number_486(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(286.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 486))

	def test_number_487(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(287.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 487))

	def test_number_488(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(288.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 488))

	def test_number_489(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(289.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 489))

	def test_number_490(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(290.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 490))

	def test_number_491(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(291.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 491))

	def test_number_492(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(292.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 492))

	def test_number_493(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(293.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 493))

	def test_number_494(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(294.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 494))

	def test_number_495(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(295.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 495))

	def test_number_496(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(296.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 496))

	def test_number_497(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(297.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 497))

	def test_number_498(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(298.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 498))

	def test_number_499(self):
		input = Program([ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([Return(FloatLiteral(299.0))]))])])
		expect = ''
		self.assertTrue(TestCodeGen.test(input, expect, 499))

