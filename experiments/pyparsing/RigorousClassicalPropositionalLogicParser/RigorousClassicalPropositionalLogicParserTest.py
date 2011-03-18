# Tests for A rigorous parser for Classical Propositional Logic
# Author: Adolfo Neto
# 16/03/2011
#

from RigorousClassicalPropositionalLogicParser import RigorousClassicalPropositionalLogicParser, Formula
import unittest
 
class RigorousClassicalPropositionalLogicParser_TestCase(unittest.TestCase):
	def setUp(self):
		self.parser = RigorousClassicalPropositionalLogicParser()

	def parseFormula(self,text):
		f = Formula(self.parser.parse(text).asList()[0])
		return f

	def testAtomicFormula(self):
		self.assertEquals("A1", str(self.parseFormula("A1")))
		self.assertEquals(None, self.parseFormula("A1").connective)

	def testUnaryComplexityTwoFormula(self):
		self.assertEquals("(! A1)", str(self.parseFormula("!A1")))
		self.assertEquals("!", self.parseFormula("!A1").connective)

	def testUnaryComplexityThreeFormula(self):
		self.assertEquals("(! (! A12))", str(self.parseFormula("!!A12")))
		self.assertEquals("!", self.parseFormula("!!A12").connective)

	def testBinaryComplexityThreeFormula(self):
		self.assertEquals("(& A B)", str(self.parseFormula("(A&B)")))
		self.assertEquals("&", self.parseFormula("(A&B)").connective)

	def testBinaryComplexityFiveFormula(self):
		self.assertEquals("(& (& A B) C23)", str(self.parseFormula("( (A&B)&C23)")))
		self.assertEquals("&", self.parseFormula("( (A&B)&C23)").connective)

	def testBinaryComplexityFiveFormula(self):
		self.assertEquals("(| (& A B) (! C23))", str(self.parseFormula("( (A&B)|!C23)")))
		self.assertEquals("|", self.parseFormula("( (A&B)|!C23)").connective)

	def testWrongAtomicFormulaWithParentheses(self):
		self.assertRaises(AttributeError,self.parseFormula,"(A)")

	def testWrongUnaryFormulaWithExtraParentheses(self):
		self.assertRaises(AttributeError,self.parseFormula,"(!A)")
		self.assertRaises(AttributeError,self.parseFormula,"!(A)")

	def testWrongBinaryFormulaWithExtraParentheses(self):
		self.assertRaises(AttributeError,self.parseFormula,"((A&B))")
 
	def testWrongBinaryFormulaWithoutParentheses(self):
		self.assertRaises(AttributeError,self.parseFormula,"A&B")



if __name__ == '__main__':
	unittest.main()



