#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# TruthAssignmentTest.py - some experiments for the Logic Dojo Tool

# a test that the student must make it pass


### O nome do arquivo editado pelo estudante tem que ser TruthAssignmentAnswer.py
from TruthAssignmentAnswer import *

### O nome do arquivo editado pelo professor definindo um TruthAssignment
### tem que ser TruthAssignmentSpec.py
from TruthAssignmentSpec import TruthAssignment
import unittest


class TruthAssignmentTest(unittest.TestCase):

    def test_andValuation(self):

## Student MUST define a truthAssignment variable
        self.assertEquals(1, truthAssignment.getValue("A&B"))


## PYTHON's PyUnit demands this

if __name__ == "__main__":
	unittest.main()
