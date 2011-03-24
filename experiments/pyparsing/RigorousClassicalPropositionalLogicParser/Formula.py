# Representation of a Classical Propositional Logic formula
# Author: Adolfo Neto
# 16/03/2011

class Formula:
	def __init__(self,parserResult):

		if (isinstance(parserResult,str)):	
			self.connective=None
			self.subformulas=parserResult
		elif (len(parserResult)==2):
			self.connective=parserResult[0]
			self.subformulas=[Formula(parserResult[1])]
		else:
			self.connective=parserResult[1]
			self.subformulas=[Formula(parserResult[0]),Formula(parserResult[2])]

	def __str__(self):
		if self.connective!=None:
			subformulas_as_string = " ".join(map(str,self.subformulas))
			return "("+ str(self.connective) + " " + subformulas_as_string + ")"
		else:
			return self.subformulas

	def getConnective(self):
		return "BLA"


class AtomicFormula(Formula):
	def __init__(self, atomString):
		self.atom = atomString
	def getConnective(self):
		return None
	def __str__(self):
		return self.atom

class UnaryFormula(Formula):
	def __init__(self, connective, subformula):
		self.connective = connective
		self.subformula = subformula
	def getConnective(self):
		return self.connective
	def __str__(self):
		return str(self.connective) + str(self.subformula)

class BinaryFormula(Formula):
	def __init__(self, connective, leftSubformula, rightSubformula):
		self.connective = connective
		self.leftSubformula = leftSubformula
		self.rightSubformula = rightSubformula
	def getConnective(self):
		return self.connective
	def __str__(self):
		return "(" + str(self.leftSubformula) + str(self.connective) + str(self.rightSubformula) + ")"

class FormulaFactory:
	def __init__(self):
		pass

	def createAtomicFormula(self, atomString):
		return AtomicFormula(atomString)
	
	def createUnaryFormula(self, connective, subformula):
		return UnaryFormula(connective, subformula)

	def createBinaryFormula(self, connective, leftSubformula, rightSubformula):
		return BinaryFormula(connective, leftSubformula, rightSubformula)
		
