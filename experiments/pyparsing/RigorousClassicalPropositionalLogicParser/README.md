A "Rigorous" Parser for Classical Propositional Logic
=====================================================

Author: [Adolfo Neto](http://twitter.com/adolfont)


Motivation
----------

Some parsers for Classical Propositional Logic allow:

* the optional use of parentheses. For instance, one can write "A&B" or "(A&B)".
* the n-ary use of binary connectives. For instance, one can write "A&B&C" meaning "((A&B)&C)".
 * In this case, precedence and associativity rules are need in order to distinguish, for instance, "A&B|C" from "A&(B|C)".

This is not the case with this parser. This parser for Classical Propositional Logic that strictly follows the rules in the Silva-Finger-Melo book: 

* [Logic for Computing](http://bit.ly/fqbyF4) ("Logica para Computacao", in Portuguese).


Important notes
---------------

In this parser, parenthesis cannot be omitted!

We have four connectives: "!" (negation, unary) , "&" (conjuntion, binary), "|" (disjunction, binary),  "->" (implication, binary)


Dependencies
------------

This parser uses the excellent [Paul McGuire's "pyparsing" module for Python.](http://pyparsing.wikispaces.com/)



