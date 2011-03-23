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


class FormulaFactory:
	def __init__(self):
		pass

	def createAtomicFormula(self, atomString):
		return AtomicFormula(atomString)
	
	def createUnaryFormula(self, connective, subformula):
		return UnaryFormula(connective, subformula)

		
