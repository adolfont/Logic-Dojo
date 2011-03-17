# A parser for Classical Propositional Logic
# Author: Adolfo Neto
# 16/03/2011
#
# This parser for Classical Propositional Logic follows exactly the rules in the Silva-Finger-Melo book: 
# "Logic for Computing" ("Logica para Computacao" in Portuguese)
# Link for the book: http://bit.ly/fqbyF4
#
# Important notes: 

# In this parser, parenthesis cannot be omitted!
# We have four connectives: "!" (negation, unary) , "&" (conjuntion, binary), "|" (disjunction, binary),  "->" (implication, binary)

# This parser uses the excellent Paul McGuire's "pyparsing" module for Python: http://pyparsing.wikispaces.com/


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
		self.left_parenthesis = "("
		self.right_parenthesis = ")"
		self.implies = Literal("->")
		self.or_ = Literal("|")
		self.and_ = Literal("&")
		self.not_ = Literal("!") | Literal ("~")
		self.boolean = Keyword("false") | Keyword("true")
		self.symbol = Word(alphas, alphanums)

		self.formula = Forward()
		self.operand = self.boolean | self.symbol

		self.binary_connective = self.or_ | self.and_ | self.implies

		self.unaryFormula = self.not_ + self.formula
		self.binaryFormula = self.left_parenthesis + self.formula + self.binary_connective + self.formula + self.right_parenthesis

		self.formula << (self.unaryFormula | self.binaryFormula | self.operand)

	def parse(self,text):
		try:
			result = self.formula.parseString(text, parseAll=True)
#			assert len(result) == 1
			return  result
#Old version			
#			resultList = list()
#			if (isinstance(result[0],str)):
#				resultList.append(result[0])
#			else:
#				resultList.append(result[0].asList())
#
#			return resultList

		except (ParseException, ParseSyntaxException) as err:
			print("Syntax error:\n{0.line}\n{1}^".format(err, " " * (err.column - 1)))
			return ""


parser = CPL_Parser()

print parser.parse("A")
print parser.parse("A1")
print parser.parse("!A")
print parser.parse("!!A12")
print parser.parse("(A&B1)")
print parser.parse("((A&B1)&C23)")
print parser.parse("((A|B1)->!C23)")








