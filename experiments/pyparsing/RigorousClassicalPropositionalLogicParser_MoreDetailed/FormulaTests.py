# Tests for the class that represents formulas
# Author: Adolfo Neto
# 23/03/2011
#

from ClassicalPropositionalLogicFormulaFactory import *
import unittest
 
class Formula_TestCase(unittest.TestCase):
	def setUp(self):
		self.formulaFactory = ClassicalPropositionalLogicFormulaFactory()
		self.cpl = self.formulaFactory.logic
		self.anAtomicFormula = self.formulaFactory.createAtom("A")
		self.anUnaryFormula = self.formulaFactory.createNegation(self.anAtomicFormula)
		self.aSizeThreeUnaryFormula = self.formulaFactory.createNegation(self.anUnaryFormula)
		self.aBinaryFormula = self.formulaFactory.createConjunction(self.anAtomicFormula, self.anAtomicFormula)
		self.anotherAtomicFormula = self.formulaFactory.createAtom("B")
		self.anotherBinaryFormula = self.formulaFactory.createConjunction(self.anAtomicFormula, self.anotherAtomicFormula)
		self.aSizeSixFormula = self.formulaFactory.createImplication(self.anUnaryFormula, self.anotherBinaryFormula)


	def testAtomicFormula_getConnective(self):
		self.assertEquals(None,self.anAtomicFormula.getConnective())

	def testAtomicFormula_toString(self):
		self.assertEquals("A",str(self.anAtomicFormula))

	def testSizeTwoUnaryFormula_getConnective(self):
		self.assertEquals(self.cpl.NOT,self.anUnaryFormula.getConnective())

	def testSizeTwoUnaryFormula_toString(self):
		self.assertEquals("!A",str(self.anUnaryFormula))

	def testSizeThreeUnaryFormula_getConnective(self):
		self.assertEquals(self.cpl.NOT,self.aSizeThreeUnaryFormula.getConnective())

	def testSizeThreeUnaryFormula_toString(self):
		self.assertEquals("!!A",str(self.aSizeThreeUnaryFormula))

	def testSizeThreeBinaryFormula_getConnective(self):
		self.assertEquals(self.cpl.AND,self.aBinaryFormula.getConnective())
		
	def testSizeThreeBinaryFormula_toString(self):
		self.assertEquals("(A&A)",str(self.aBinaryFormula))

	def testSizeSixBinaryFormula_getConnective(self):
		self.assertEquals(self.cpl.IMPLIES,self.aSizeSixFormula.getConnective())
		
	def testSizeSixBinaryFormula_toString(self):
		self.assertEquals("(!A->(A&B))",str(self.aSizeSixFormula))




if __name__ == '__main__':
	unittest.main()

