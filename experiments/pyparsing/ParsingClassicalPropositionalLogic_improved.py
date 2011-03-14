# 14/03/2011
# Parsing Classical Propositional Logic
# Adolfo Neto

# Adapted from "Parsing First-Order Logic"
# pp. 548-553
# Programming in Python 3, Mark Summerfield
# Second Edition, 2010
# In the book the author uses Python 3 and pyparsing_py3


from pyparsing import (alphanums, alphas, delimitedList, Forward, Group,
	 Keyword, Literal, opAssoc, operatorPrecedence, ParserElement,
	 ParseException, ParseSyntaxException, Suppress, Word)

ParserElement.enablePackrat()

class Operand(object):
    def __init__(self,t):
        self.args = t[0][0::2]
    def __str__(self):
        sep = " %s " % self.reprsymbol
        return "[" + sep.join(map(str,self.args)) + "]"

class NotConnective(Operand):
	reprsymbol = '!'
	def __init__(self,t):
		self.arg = t[0][1]
	def __str__(self):
		return self.reprsymbol + str(self.arg)
	def asList(self):
		result = []
		result.append(self.reprsymbol)
		if (isinstance(self.arg,str)):
			result.append(self.arg)
		else:
			result.append(self.arg.asList())
		return result


class AndConnective(Operand):
	reprsymbol = '&'
	def asList(self):
		result = []
		result.append(self.reprsymbol)
		for arg in self.args:
			if (isinstance(arg,str)):
				result.append(arg)
			else:
				result.append(arg.asList())
		return result


class OrConnective(Operand):
	reprsymbol = '|'
	def asList(self):
		result = []
		result.append(self.reprsymbol)
		for arg in self.args:
			if (isinstance(arg,str)):
				result.append(arg)
			else:
				result.append(arg.asList())
		return result

class ImpliesConnective(Operand):
	reprsymbol = '->'
	def asList(self):
		result = []
		result.append(self.reprsymbol)
		for arg in self.args:
			if (isinstance(arg,str)):
				result.append(arg)
			else:
				result.append(arg.asList())
		return result



left_parenthesis, right_parenthesis = map(Suppress, "()")
implies = Literal("->")
or_ = Literal("|")
and_ = Literal("&")
not_ = Literal("!") | Literal ("~")
boolean = Keyword("false") | Keyword("true")
symbol = Word(alphas, alphanums)

formula = Forward()
operand = boolean | symbol

formula << operatorPrecedence(operand, [
				(not_, 1, opAssoc.RIGHT, NotConnective),
				(and_, 2, opAssoc.LEFT, AndConnective),
				(or_, 2, opAssoc.LEFT, OrConnective),
				(implies, 2, opAssoc.RIGHT, ImpliesConnective)])

def parse(text):

	try:
		result = formula.parseString(text, parseAll=True)
		assert len(result) == 1

		if (isinstance(result[0],str)):
			resultList = list()
			resultList.append(result[0])
			return resultList
		else:
			return result[0].asList()

	except (ParseException, ParseSyntaxException) as err:
		print("Syntax error:\n{0.line}\n{1}^".format(err, " " * (err.column - 1)))
		return ""



sample_formulas=[
	"A",
	"A1",
	"!A1",
	"!!A1",
	"!!!A11",
	"!!!!!A23",
	"A&B",
	"A&B&C",
	"A|B",
	"A->B",
	"A|!B",
	"!A|B",
	"A->!!B",
	"!A&!B",
	"!A->(!B&(!A|C|D))",
	"!A->!B&!A|C|D",
]

for sample_formula in sample_formulas:
	print sample_formula,  " ===> ", parse(sample_formula)

print "This is the end..."

#results
'''
A  ===>  ['A']
A1  ===>  ['A1']
!A1  ===>  ['!', 'A1']
!!A1  ===>  ['!', ['!', 'A1']]
!!!A11  ===>  ['!', ['!', ['!', 'A11']]]
!!!!!A23  ===>  ['!', ['!', ['!', ['!', ['!', 'A23']]]]]
A&B  ===>  ['&', 'A', 'B']
A&B&C  ===>  ['&', 'A', 'B', 'C']
A|B  ===>  ['|', 'A', 'B']
A->B  ===>  ['->', 'A', 'B']
A|!B  ===>  ['|', 'A', ['!', 'B']]
!A|B  ===>  ['|', ['!', 'A'], 'B']
A->!!B  ===>  ['->', 'A', ['!', ['!', 'B']]]
!A&!B  ===>  ['&', ['!', 'A'], ['!', 'B']]
!A->(!B&(!A|C|D))  ===>  ['->', ['!', 'A'], ['&', ['!', 'B'], ['|', ['!', 'A'], 'C', 'D']]]
!A->!B&!A|C|D  ===>  ['->', ['!', 'A'], ['|', ['&', ['!', 'B'], ['!', 'A']], 'C', 'D']]
This is the end...
'''

# open issues/problems

# why moving "asList()" up to the Operand class does not work???

# A&B&C  ===>  ['&', 'A', 'B', 'C']
# would it better to be ['&', 'A', ['&', 'B', 'C']]  --> EXPONENTIAL GROWTH???

# how can I remove "if (isinstance(result[0],str)):"?








