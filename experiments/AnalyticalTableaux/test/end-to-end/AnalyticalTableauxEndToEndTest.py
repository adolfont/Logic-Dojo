# An end-to-end test for the analytical tableau prover

from AnalyticalTableauxProver import *
from ProblemParser import *
import unittest


class ApplicationRunnerEndToEndTest:

	def __init__(self):
		self.prover = AnalyticalTableauxProver()
		self.parser = ProblemParser()

	def run(self):
		self.parseProblem()
		self.buildProof()
		self.showProof()

	def parseProblem(self):
		self.problem = self.parser.parseFile("sample.prove")

	def buildProof(self):
		self.proof = self.prover.buildProof(self.problem)

	def showProof(self):
		print str(self.proof)




#assert problem is not null
#assert problem has 4 signed formulas

#proof = analyticalTableauProver.buildProof(problem)

#assert proof.isClosed()

#assert proof.toSimpleString() equals to
#problem.toSimpleString()+ readFile(sample.proof)


runner = ApplicationRunnerEndToEndTest()
runner.run()



