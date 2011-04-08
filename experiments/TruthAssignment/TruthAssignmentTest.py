# An end-to-end test for the analytical tableau prover inspired by #GOOS end-to-end test in http://bit.ly/hRn12J

from TruthAssignment import *

import unittest

import sys
sys.path.append("../pyparsing/RigorousClassicalPropositionalLogicParser_MoreDetailed/")
from RigorousClassicalPropositionalLogicParser import *
from FormulaFactory import *

class TruthAssignmentTest(unittest.TestCase):

	def setUp(self):
		self.assignment = TruthAssignment()
		self.parser = RigorousClassicalPropositionalLogicParser()
		self.p = self.parser.parse("p")
		self.q = self.parser.parse("q")
		self.assignment.set(self.p,1)
		self.assignment.set(self.q,0)


	def parseFormula(self,text):
		ff = FormulaFactory()
		f = ff.createFormulaFromParserResult(self.parser.parse(text).asList()[0])
		return f


	def testFirstAtomAssignmentIsCorrect(self):
		self.assertEquals(1, self.assignment.get(self.p))
	
	def testSecondAtomAssignmentIsCorrect(self):
		self.assertEquals(0, self.assignment.get(self.q))

	def testNegationOfFirstAtom(self):
		self.not_p = self.parseFormula("!p")
		print self.not_p
#		self.assertEquals(0, self.assignment.get(self.not_p))



if __name__ == '__main__':
	unittest.main()

