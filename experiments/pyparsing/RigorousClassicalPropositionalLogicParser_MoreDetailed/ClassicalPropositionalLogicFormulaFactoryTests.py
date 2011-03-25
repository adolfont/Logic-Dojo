# Tests for the factory that creates classical propositional logic formulas
# Author: Adolfo Neto
# 25-03-2011

from ClassicalPropositionalLogicFormulaFactory import *
import unittest
 
class ClassicalPropositionalLogicFormulaFactory_TestCase(unittest.TestCase):
	def setUp(self):
		self.factory = ClassicalPropositionalLogicFormulaFactory()
		self.anAtomicFormula = self.factory.createAtom("A")
		self.anotherAtomicFormula = self.factory.createAtom("B")

	def testCreateAtom_getConnective(self):	
		self.assertEquals(None, self.anAtomicFormula.getConnective())

	def testCreateAtom_toString(self):	
		self.assertEquals("A", str(self.anAtomicFormula))

	def testCreateNegation_getConnective(self):	
		self.assertEquals(self.factory.logic.NOT, self.factory.createNegation(self.anAtomicFormula).getConnective())

	def testCreateNegation_toString(self):	
		self.assertEquals("!A", str(self.factory.createNegation(self.anAtomicFormula)))

	def testCreateConjunction_getConnective(self):	
		self.assertEquals(self.factory.logic.AND, self.factory.createConjunction(self.anAtomicFormula,self.anotherAtomicFormula).getConnective())

	def testCreateConjunction_toString(self):	
		self.assertEquals("(A&B)", str(self.factory.createConjunction(self.anAtomicFormula,self.anotherAtomicFormula)))

	def testCreateDisjunction_getConnective(self):	
		self.assertEquals(self.factory.logic.OR, self.factory.createDisjunction(self.anAtomicFormula,self.anotherAtomicFormula).getConnective())

	def testCreateDisjunction_toString(self):	
		self.assertEquals("(A|B)", str(self.factory.createDisjunction(self.anAtomicFormula,self.anotherAtomicFormula)))

	def testCreateImplication_getConnective(self):	
		self.assertEquals(self.factory.logic.IMPLIES, self.factory.createImplication(self.anAtomicFormula,self.anotherAtomicFormula).getConnective())

	def testCreateImplication_toString(self):	
		self.assertEquals("(A->B)", str(self.factory.createImplication(self.anAtomicFormula,self.anotherAtomicFormula)))


if __name__ == '__main__':
	unittest.main()
