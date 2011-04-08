# truth assignments for classical propositional logic


class TruthAssignment:

	def __init__(self):
		self.assignments = dict()


	def set(self, atom, value):
		self.assignments[atom]=value		

	def get(self, atom):
		return self.assignments[atom]
