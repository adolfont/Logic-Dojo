# Tests for the rigorous parser for Classical Propositional Logic
# Author: Adolfo Neto
# 16/03/2011


from pyparsing import (alphanums, alphas, delimitedList, Forward, Group,
	 Keyword, Literal, opAssoc, operatorPrecedence, ParserElement,
	 ParseException, ParseSyntaxException, Suppress, Word)

ParserElement.enablePackrat()

class RigorousClassicalPropositionalLogicParser:

	def __init__(self):
		self.left_parenthesis = Suppress("(")
		self.right_parenthesis = Suppress(")")
		self.implies = Literal("->")
		self.or_ = Literal("|")
		self.and_ = Literal("&")
		self.not_ = Literal("!") | Literal ("~")
		self.boolean = Keyword("false") | Keyword("true")
		self.symbol = Word(alphas, alphanums)

		self.formula = Forward()
		self.operand = self.boolean | self.symbol

		self.binary_connective = self.or_ | self.and_ | self.implies

		self.unaryFormula = Group(self.not_ + self.formula)
		self.binaryFormula = Group(self.left_parenthesis + self.formula + self.binary_connective + self.formula + self.right_parenthesis)

		self.formula << (self.unaryFormula | self.binaryFormula | self.operand)

	def parse(self,text):
		try:
			result = self.formula.parseString(text, parseAll=True)
			assert len(result) == 1

			return  result

		except (ParseException, ParseSyntaxException) as err:
#			print("Syntax error:\n{0.line}\n{1}^".format(err, " " * (err.column - 1)))
			return ""
		


class Formula:
	def __init__(self,parserResult):

		if (isinstance(parserResult,str)):	
			self.connective=None
			self.subformulas=parserResult
		elif (len(parserResult)==2):
			self.connective=parserResult[0]
			self.subformulas=[Formula(parserResult[1])]
		else:
			self.connective=parserResult[1]
			self.subformulas=[Formula(parserResult[0]),Formula(parserResult[2])]

	def __str__(self):

		if self.connective!=None:
			subformulas_as_string = " ".join(map(str,self.subformulas))
			return "("+ str(self.connective) + " " + subformulas_as_string + ")"
		else:
			return self.subformulas


