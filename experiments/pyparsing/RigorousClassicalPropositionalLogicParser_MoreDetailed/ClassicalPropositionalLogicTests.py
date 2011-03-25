# Tests for the class that represents classical propositional logic
# Author: Adolfo Neto
# 25/03/2011
#

from ClassicalPropositionalLogic import *
import unittest
 
class ClassicalPropositionalLogic_TestCase(unittest.TestCase):
	def setUp(self):
		self.logic = ClassicalPropositionalLogic()

	def testGetNot(self):
		self.assertEquals("!",str(self.logic.NOT))
	def testGetAnd(self):
		self.assertEquals("&",str(self.logic.AND))
	def testGetOr(self):
		self.assertEquals("|",str(self.logic.OR))
	def testGetImplies(self):
		self.assertEquals("->",str(self.logic.IMPLIES))


if __name__ == '__main__':
	unittest.main()
