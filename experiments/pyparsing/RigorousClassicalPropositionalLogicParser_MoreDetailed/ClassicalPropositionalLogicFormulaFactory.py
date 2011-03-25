# A factory that creates classical propositional logic formulas
# Author: Adolfo Neto
# 25-03-2011

from ClassicalPropositionalLogic import *
from FormulaFactory import *

class ClassicalPropositionalLogicFormulaFactory(FormulaFactory):
	def __init__(self):
		self.logic = ClassicalPropositionalLogic()

	def createAtom(self, atomString):
		return AtomicFormula(atomString)
	
	def createNegation(self,formula):
		return UnaryFormula(self.logic.NOT, formula)

	def createConjunction(self,leftSubformula, rightSubformula):
		return BinaryFormula(self.logic.AND, leftSubformula, rightSubformula)

	def createDisjunction(self,leftSubformula, rightSubformula):
		return BinaryFormula(self.logic.OR, leftSubformula, rightSubformula)

	def createImplication(self,leftSubformula, rightSubformula):
		return BinaryFormula(self.logic.IMPLIES, leftSubformula, rightSubformula)
