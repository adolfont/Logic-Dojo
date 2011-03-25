# A class that prints formulas in specific ways
# Author: Adolfo Neto
# 25-03-2011

from Formula import *

class FormulaPrinter:

	def printPrefix(self, formula):

		if formula.getConnective()==None:
			return str(formula)
		else:
			subformulas_as_string = " ".join(map(self.printPrefix,formula.getSubformulas()))
			return "("+ str(formula.getConnective()) + " " + subformulas_as_string + ")"
#		else:
#			return self.subformulas


