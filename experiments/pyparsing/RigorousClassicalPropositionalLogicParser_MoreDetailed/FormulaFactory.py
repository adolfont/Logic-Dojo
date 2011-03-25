# A factory for propositional logic formulas
# Author: Adolfo Neto
# 16/03/2011

from Formula import *

class FormulaFactory:
	def __init__(self):
		pass

	def createAtomicFormula(self, atomString):
		return AtomicFormula(atomString)
	
	def createUnaryFormula(self, connective, subformula):
		return UnaryFormula(connective, subformula)

	def createBinaryFormula(self, connective, leftSubformula, rightSubformula):
		return BinaryFormula(connective, leftSubformula, rightSubformula)

	def createFormulaFromParserResult(self, parserResult):
		if (isinstance(parserResult,str)):	
			return self.createAtomicFormula(parserResult)
		elif (len(parserResult)==2):
			connective=parserResult[0]
			return self.createUnaryFormula(connective, self.createFormulaFromParserResult(parserResult[1]))
		else:
			connective=parserResult[1]
			return self.createBinaryFormula(connective, self.createFormulaFromParserResult(parserResult[0]),
					self.createFormulaFromParserResult(parserResult[2]))
