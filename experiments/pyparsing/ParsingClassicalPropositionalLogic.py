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
				(not_, 1, opAssoc.RIGHT),
				(and_, 2, opAssoc.LEFT),
				(or_, 2, opAssoc.LEFT),
				(implies, 2, opAssoc.RIGHT)])

def parse(text):

	try:
		result = formula.parseString(text, parseAll=True)
		assert len(result) == 1
		if isinstance(result[0],str):
			return result[0]
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
	"A&B",
	"A|B",
	"A->B",
	"A|!B",
	"!A|B",
	"A->!!B",
	"!A&!B",
	"!A!B",
]

for sample_formula in sample_formulas:
	print sample_formula,  " ===> ", parse(sample_formula)

print "This is the end..."





