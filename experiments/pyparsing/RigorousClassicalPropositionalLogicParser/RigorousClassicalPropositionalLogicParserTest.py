# Tests for a rigorous parser for Classical Propositional Logic
# Author: Adolfo Neto
# 16/03/2011
#

from RigorousClassicalPropositionalLogicParser import RigorousClassicalPropositionalLogicParser
from Formula import *
import unittest
 
class RigorousClassicalPropositionalLogicParser_TestCase(unittest.TestCase):
	def setUp(self):
		self.parser = RigorousClassicalPropositionalLogicParser()

	def parseFormula(self,text):
		ff = FormulaFactory()
		f = ff.createFormulaFromParserResult(self.parser.parse(text).asList()[0])
		return f

	def test_createAtomicFormula_toString(self):
		self.assertEquals("A1", str(self.parseFormula("A1")))

	def test_createAtomicFormula_getConnective(self):
		self.assertEquals(None, self.parseFormula("A1").getConnective())

	def test_createUnaryComplexityTwoFormula_toString(self):
		self.assertEquals("!A1", str(self.parseFormula("!A1")))
#		self.assertEquals("(! A1)", str(self.parseFormula("!A1")))

	def test_createUnaryComplexityTwoFormula_getConnective(self):
		self.assertEquals("!", self.parseFormula("!A1").getConnective())

	def test_createUnaryComplexityThreeFormula_toString(self):
		self.assertEquals("!!A12", str(self.parseFormula("!!A12")))
#		self.assertEquals("(! (! A12))", str(self.parseFormula("!!A12")))

	def test_createUnaryComplexityThreeFormula_getConnective(self):
		self.assertEquals("!", self.parseFormula("!!A12").getConnective())

	def test_createBinaryComplexityThreeFormula_toString(self):
		self.assertEquals("(A&B)", str(self.parseFormula("(A&B)")))
#		self.assertEquals("(& A B)", str(self.parseFormula("(A&B)")))

	def test_createBinaryComplexityThreeFormula_getConnective(self):
		self.assertEquals("&", self.parseFormula("(A&B)").getConnective())

	def test_createBinaryComplexityFiveFormula_toString(self):
		self.assertEquals("((A&B)&C23)", str(self.parseFormula("( (A&B)&C23)")))
#		self.assertEquals("(& (& A B) C23)", str(self.parseFormula("( (A&B)&C23)")))

	def test_createBinaryComplexityFiveFormula_getConnective(self):
		self.assertEquals("&", self.parseFormula("( (A&B)&C23)").getConnective())

	def test_createBinaryComplexitySixFormula_toString(self):
		self.assertEquals("((A&B)|!C23)", str(self.parseFormula("( (A&B)|!C23)")))
#		self.assertEquals("(| (& A B) (! C23))", str(self.parseFormula("( (A&B)|!C23)")))

	def test_createBinaryComplexitySixFormula_getConnective(self):
		self.assertEquals("|", self.parseFormula("( (A&B)|!C23)").getConnective())

	def test_WrongAtomicFormulaWithParentheses(self):
		self.assertRaises(AttributeError,self.parseFormula,"(A)")

	def test_WrongUnaryFormulaWithExtraParentheses(self):
		self.assertRaises(AttributeError,self.parseFormula,"(!A)")
		self.assertRaises(AttributeError,self.parseFormula,"!(A)")

	def test_WrongBinaryFormulaWithExtraParentheses(self):
		self.assertRaises(AttributeError,self.parseFormula,"((A&B))")
 
	def test_WrongBinaryFormulaWithoutParentheses(self):
		self.assertRaises(AttributeError,self.parseFormula,"A&B")



if __name__ == '__main__':
	unittest.main()



