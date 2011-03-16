# 16/03/2011
# A parser for Classical Propositional Logic
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





class CPL_Parser:

	def __init__(self):
		self.left_parenthesis, self.right_parenthesis = map(Suppress, "()")
		self.implies = Literal("->")
		self.or_ = Literal("|")
		self.and_ = Literal("&")
		self.not_ = Literal("!") | Literal ("~")
		self.boolean = Keyword("false") | Keyword("true")
		self.symbol = Word(alphas, alphanums)

		self.formula = Forward()
		self.operand = self.boolean | self.symbol

		self.formula << operatorPrecedence(self.operand, [
				(self.not_, 1, opAssoc.RIGHT, NotConnective),
				(self.and_, 2, opAssoc.LEFT, AndConnective),
				(self.or_, 2, opAssoc.LEFT, OrConnective),
				(self.implies, 2, opAssoc.RIGHT, ImpliesConnective)])


	def parse(self,text):
		try:
			result = self.formula.parseString(text, parseAll=True)
			assert len(result) == 1

			
			resultList = list()
			if (isinstance(result[0],str)):
				resultList.append(result[0])
			else:
				resultList.append(result[0].asList())

			return resultList
		except (ParseException, ParseSyntaxException) as err:
			print("Syntax error:\n{0.line}\n{1}^".format(err, " " * (err.column - 1)))
			return ""











