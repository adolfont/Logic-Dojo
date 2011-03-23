# Tests for the class that represents formulas
# Author: Adolfo Neto
# 23/03/2011
#

from Formula import *
import unittest
 
class Formula_TestCase(unittest.TestCase):
	def testAtomicFormula_getConnective(self):
		self.assertEquals(None,FormulaFactory().createAtomicFormula("A").getConnective())

	def testAtomicFormula_toString(self):
		self.assertEquals("A",str(FormulaFactory().createAtomicFormula("A")))


if __name__ == '__main__':
	unittest.main()

