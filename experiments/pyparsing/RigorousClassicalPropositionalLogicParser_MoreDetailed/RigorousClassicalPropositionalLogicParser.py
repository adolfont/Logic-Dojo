# A rigorous parser for Classical Propositional Logic formulas
# Author: Adolfo Neto
# 16/03/2011


from pyparsing import (alphanums, alphas, delimitedList, Forward, Group,
	 Keyword, Literal, opAssoc, operatorPrecedence, ParserElement,
	 ParseException, ParseSyntaxException, Suppress, Word)

from Formula import *

ParserElement.enablePackrat()


### BNF

# formula = operand | unaryFormula | binaryFormula
# unaryFormula = ("!"|"~") + formula
# binaryFormula = "(" + formula + binaryConnective + formula + ")"
# binaryConnective = "&" | "|" | "->"
# operand = "true" | "false" | symbol
# symbol = alpha + alphanums*

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

		self.binaryConnective = self.or_ | self.and_ | self.implies

		self.unaryFormula = Group(self.not_ + self.formula)
		self.binaryFormula = Group(self.left_parenthesis + self.formula + self.binaryConnective + self.formula + self.right_parenthesis)

		self.formula << (self.unaryFormula | self.binaryFormula | self.operand)


## Should return a ParserResult object

	def parse(self,text):
		try:
			result = self.formula.parseString(text, parseAll=True)
			assert len(result) == 1

			return  result

		except (ParseException, ParseSyntaxException) as err:
#			print("Syntax error:\n{0.line}\n{1}^".format(err, " " * (err.column - 1)))
			return ""
		




