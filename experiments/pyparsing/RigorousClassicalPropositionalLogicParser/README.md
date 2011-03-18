Rigorous Classical Propositional Logic Parser
=============================================



Most parsers for Classical Propositional Logic allow:
* the optional use of parenthesis
* the nary use of binary connectives

This is not the case with this parser. This parser for Classical Propositional Logic follows exactly the rules in the Silva-Finger-Melo book: 
* "Logic for Computing" ("Logica para Computacao" in Portuguese). Link for the book: http://bit.ly/fqbyF4


Important notes
---------------

In this parser, parenthesis cannot be omitted!

We have four connectives: "!" (negation, unary) , "&" (conjuntion, binary), "|" (disjunction, binary),  "->" (implication, binary)


Dependencies
------------

This parser uses the excellent Paul McGuire's "pyparsing" module for Python: http://pyparsing.wikispaces.com/


Author
-------

Adolfo Neto
