#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# logicdojo_tests.py - tests for the logic dojo class

from logicdojo import *
import unittest

class TestLogicDojo(unittest.TestCase):

	def setUp(self):
		self.dojo = LogicDojo()

	def testDojoNotNone(self):
		self.assertNotEquals(None,self.dojo)

	def testDojoShouldCorrectlyParseATestFile(self):
		self.assertTrue(self.dojo.parseTest("01_valuation_test.ldj"))

if __name__ == "__main__":
	unittest.main()

