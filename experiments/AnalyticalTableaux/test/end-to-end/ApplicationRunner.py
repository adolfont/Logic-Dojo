# An application runner for the analytical tableau prover, inspired by #GOOS application runner in http://bit.ly/eG5M9G

from AnalyticalTableauxProver import *
from ProblemParser import *


class ApplicationRunner():

	def __init__(self):
		self.prover = AnalyticalTableauxProver()
		self.parser = ProblemParser()

	def runProver(self):
		self.parseProblem()
		self.buildProof()

	def parseProblem(self):
		self.problem = self.parser.parseFile("sample.prove")

	def buildProof(self):
		self.proof = self.prover.buildProof(self.problem)

	def getProof(self):
		return self.proof



