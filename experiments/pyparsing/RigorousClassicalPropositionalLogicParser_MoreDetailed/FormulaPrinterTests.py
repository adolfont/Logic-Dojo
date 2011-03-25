# Tests for a class that prints formulas in specific ways
# Author: Adolfo Neto
# 25-03-2011

from FormulaPrinter import *
from FormulaFactory import *
from RigorousClassicalPropositionalLogicParser import RigorousClassicalPropositionalLogicParser
import unittest

class FormulaPrinterTests_TestCase(unittest.TestCase):
	def setUp(self):
		self.parser = RigorousClassicalPropositionalLogicParser()	
		self.formulaPrinter = FormulaPrinter()

		self.atom = self.parseFormula("A1")
		self.negation = self.parseFormula("!A1")
		self.size3negation = self.parseFormula("!!A1")
		self.conjunction = self.parseFormula("(A1&B2)")

	def parseFormula(self,text):
		ff = FormulaFactory()
		f = ff.createFormulaFromParserResult(self.parser.parse(text).asList()[0])
		return f

	def test_printAtom(self):
		self.assertEquals("A1", self.formulaPrinter.printPrefix(self.atom))

	def test_printNegation(self):
		self.assertEquals("(! A1)", self.formulaPrinter.printPrefix(self.negation))

	def test_printSize3Negation(self):
		self.assertEquals("(! (! A1))", self.formulaPrinter.printPrefix(self.size3negation))

	def test_printConjunction(self):
		self.assertEquals("(& A1 B2)", self.formulaPrinter.printPrefix(self.conjunction))

	def test_printSize5BinaryFormula(self):
		self.assertEquals("(& (& A B) C23)", self.formulaPrinter.printPrefix(self.parseFormula("( (A&B)&C23)")))

	def test_printSize6BinaryFormula(self):
		self.assertEquals("(| (& A B) (! C23))", self.formulaPrinter.printPrefix(self.parseFormula("( (A&B)|!C23)")))



if __name__ == '__main__':
	unittest.main()



