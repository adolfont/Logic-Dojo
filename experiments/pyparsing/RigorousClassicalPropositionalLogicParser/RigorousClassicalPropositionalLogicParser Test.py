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
			print("Syntax error:\n{0.line}\n{1}^".format(err, " " * (err.column - 1)))
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
			subf = ""
			for i in self.subformulas:
				subf = subf + str(i) + " "
			return "("+ str(self.connective) + " " + subf + ")"
		else:
			return self.subformulas

parser = RigorousClassicalPropositionalLogicParser()

#print parser.parse("A")
#print parser.parse("A1")
#print parser.parse("!A")
#print parser.parse("!!A12")
#print parser.parse("(A&B1)")
#print parser.parse("((A&B1)&C23)")
#print parser.parse("((A|B1)->!C23)")


def parseFormula(text):
	f = Formula(parser.parse(text).asList()[0])
#	print "texto da formula:", texto 
#	print "resultado do parsing: ", parser.parse(texto)
#	print f
	return f
	
print(parseFormula("(A&B)"))


import unittest
 
class CPL_SFM06_TestCase(unittest.TestCase):
	def testAtomicFormula(self):
		self.assertEquals("A1", str(parseFormula("A1")))
		self.assertEquals(None, parseFormula("A1").connective)
	def testUnaryComplexityTwoFormula(self):
		self.assertEquals("(! A1 )", str(parseFormula("!A1")))
		self.assertEquals("!", parseFormula("!A1").connective)
	def testUnaryComplexityThreeFormula(self):
		self.assertEquals("(! (! A12 ) )", str(parseFormula("!!A12")))
		self.assertEquals("!", parseFormula("!!A12").connective)
	def testBinaryComplexityThreeFormula(self):
		self.assertEquals("(& A B )", str(parseFormula("(A&B)")))
		self.assertEquals("&", parseFormula("(A&B)").connective)
 
if __name__ == '__main__':
	unittest.main()

