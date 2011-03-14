# 14/03/2011
# Parsing Classical Propositional Logic
# Adolfo Neto

# Adapted from "Parsing First-Order Logic"
# pp. 548-553
# Programming in Python 3, Mark Summerfield
# Second Edition, 2010
# In the book the author uses Python 3 and pyparsing_py3


from pyparsing import (alphanums, alphas, delimitedList, Forward, Group, Keyword, Literal, opAssoc, 
	operatorPrecedence, ParserElement, ParseException, ParseSyntaxException, Suppress, Word)
ParserElement.enablePackrat()

left_parenthesis, right_parenthesis = map(Suppress, "()")
implies = Literal("->")
or_ = Literal("|")
and_ = Literal("&")
not_ = Literal("!") | Literal ("~")
equals = Literal("=")
boolean = Keyword("false") | Keyword("true")
symbol = Word(alphas, alphanums)

formula = Forward()
operand = boolean | symbol

formula << operatorPrecedence(operand, [
				(equals, 2, opAssoc.LEFT),
				(not_, 1, opAssoc.RIGHT),
				(and_, 2, opAssoc.LEFT),
				(or_, 2, opAssoc.LEFT),
				(implies, 2, opAssoc.RIGHT)])


text="A&B&C->D"
try:
	result = formula.parseString(text, parseAll=True)
	assert len(result) == 1
	print result[0].asList()
except (ParseException, ParseSyntaxException) as err:
	print("Syntax error:\n{0.line}\n{1}^".format(err, " " * (err.column - 1)))

