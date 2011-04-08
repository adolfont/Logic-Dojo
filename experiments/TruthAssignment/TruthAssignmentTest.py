# An end-to-end test for the analytical tableau prover inspired by #GOOS end-to-end test in http://bit.ly/hRn12J

from TruthAssignment import *
import unittest

class TruthAssignmentTest(unittest.TestCase):

	def setUp(self):
		self.assignment = TruthAssignment()
		self.assignment.set("p",1)


	def testFirstAtomAssignmentIsCorrect(self):
		self.assertEquals(1, self.assignment.get("v"))
	



if __name__ == '__main__':
	unittest.main()

