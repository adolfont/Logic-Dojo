# 14/03/2011
# Parsing First-Order Logic
# pp. 548-553
# Programming in Python 3, Mark Summerfield
# Second Edition, 2010

# In the book the author uses Python 3 and pyparsing_py3


from pyparsing import (alphanums, alphas, delimitedList, Forward, Group, Keyword, Literal, opAssoc, 
	operatorPrecedence, ParserElement, ParseException, ParseSyntaxException, Suppress, Word)
ParserElement.enablePackrat()

left_parenthesis, right_parenthesis, colon = map(Suppress, "():")
forall = Keyword("forall")
exists = Keyword("exists")
implies = Literal("->")
or_ = Literal("|")
and_ = Literal("&")
not_ = Literal("!") | Literal ("~")
equals = Literal("=")
boolean = Keyword("false") | Keyword("true")
symbol = Word(alphas, alphanums)

term = Forward()
term << (Group(symbol + Group(left_parenthesis + 
		delimitedList(term) + right_parenthesis)) | symbol)

formula = Forward()
forall_expression = Group(forall + symbol + colon + formula)
exists_expression = Group(exists + symbol + colon + formula)
operand = forall_expression | exists_expression  | boolean | term

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

