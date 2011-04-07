# An end-to-end test for the analytical tableau prover inspired by #GOOS end-to-end test in http://bit.ly/hRn12J

from ApplicationRunner import *
import unittest


class AnalyticalTableauxEndToEndTest(unittest.TestCase):

	def setUp(self):
		self.applicationRunner = ApplicationRunner()


	def testRunProverAndCheckProof(self):
		self.applicationRunner.runProver()
		self.assertEquals(None,self.applicationRunner.getProof())


if __name__ == '__main__':
	unittest.main()


