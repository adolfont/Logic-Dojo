# Representation of a Classical Propositional Logic formula
# Author: Adolfo Neto
# 16/03/2011


class ClassicalPropositionalLogic:
	def __init__(self):
		self.NOT = "!"
		self.AND = "&"
		self.OR = "|"
		self.IMPLIES = "->"

class Formula:
	pass

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




