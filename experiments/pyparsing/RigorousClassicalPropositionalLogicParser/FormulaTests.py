# Tests for the class that represents formulas
# Author: Adolfo Neto
# 23/03/2011
#

from Formula import *
import unittest
 
class Formula_TestCase(unittest.TestCase):
	def setUp(self):
		self.formulaFactory = FormulaFactory()
		self.anAtomicFormula = self.formulaFactory.createAtomicFormula("A")
		self.anUnaryFormula = self.formulaFactory.createUnaryFormula("!",
								self.anAtomicFormula)
		self.aComplexityThreeUnaryFormula = self.formulaFactory.createUnaryFormula(
								"!",self.anUnaryFormula)
		self.aBinaryFormula = self.formulaFactory.createBinaryFormula(
								"&",self.anAtomicFormula, self.anAtomicFormula)
		self.anotherAtomicFormula = self.formulaFactory.createAtomicFormula("B")
		self.anotherBinaryFormula = self.formulaFactory.createBinaryFormula(
								"&",self.anAtomicFormula, self.anotherAtomicFormula)
		self.aComplexitySixFormula = self.formulaFactory.createBinaryFormula(
								"->", self.anUnaryFormula, self.anotherBinaryFormula)


	def testAtomicFormula_getConnective(self):
		self.assertEquals(None,self.anAtomicFormula.getConnective())

	def testAtomicFormula_toString(self):
		self.assertEquals("A",str(self.anAtomicFormula))

	def testComplexityTwoUnaryFormula_getConnective(self):
		self.assertEquals("!",self.anUnaryFormula.getConnective())

	def testComplexityTwoUnaryFormula_toString(self):
		self.assertEquals("!A",str(self.anUnaryFormula))

	def testComplexityThreeUnaryFormula_getConnective(self):
		self.assertEquals("!",self.aComplexityThreeUnaryFormula.getConnective())

	def testComplexityThreeUnaryFormula_toString(self):
		self.assertEquals("!!A",str(self.aComplexityThreeUnaryFormula))

	def testComplexityThreeBinaryFormula_getConnective(self):
		self.assertEquals("&",self.aBinaryFormula.getConnective())
		
	def testComplexityThreeBinaryFormula_toString(self):
		self.assertEquals("(A&A)",str(self.aBinaryFormula))

	def testComplexitySixBinaryFormula_getConnective(self):
		self.assertEquals("->",self.aComplexitySixFormula.getConnective())
		
	def testComplexitySixBinaryFormula_toString(self):
		self.assertEquals("(!A->(A&B))",str(self.aComplexitySixFormula))


if __name__ == '__main__':
	unittest.main()

