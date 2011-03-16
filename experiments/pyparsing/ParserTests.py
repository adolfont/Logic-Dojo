#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# ParserTests.py - some experiments for the Logic Dojo Tool parser


from CPL_Parser import *

import unittest

class TruthAssignmentTest(unittest.TestCase):

	def setUp(self):
		self.parser = CPL_Parser()

	def test_parserTest(self):
		self.assertEquals(0, 0)
		print self.parser.parse("P1")
		print self.parser.parse("(P2)")
		print self.parser.parse("!P")
		print self.parser.parse("(!P)")
		print self.parser.parse("P&Q")
		print self.parser.parse("P->!!R")
		print self.parser.parse("P|Q|R")

if __name__ == "__main__":
	unittest.main()

# the result is a list

# if the first element of the list is not a list
  # then it is an atomic formula
  # otherwise,
    # it's a composite formula
    # the first element of this composite formula is the connective
    # the remaining elemnents are subformulas

#define methods to identify 
  # atomic?
  # composite?

# TO DO: deal with zeroary formulas

