#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# TruthAssignmentTest_v2.py - some experiments for the Logic Dojo Tool

# a test that the student must make it pass


### O nome do arquivo editado pelo estudante tem que ser TruthAssignmentAnswer.py
from TruthAssignmentAnswer_v2 import *

### O nome do arquivo editado pelo professor definindo um TruthAssignment
### tem que ser TruthAssignmentSpec.py
from TruthAssignmentSpec import TruthAssignment
import unittest


class TruthAssignmentTest(unittest.TestCase):

    ## Student MUST define a t1 variable
    def test_andValuation(self):
        self.assertEquals(1, t1.getValue("A&B"))


    ## Student MUST define a t2 variable
    def test_verySpecialValuation(self):
        self.assertEquals(0, t2.getValue("A&B"))
        self.assertEquals(1, t2.getValue("A|B"))
#        self.assertEquals(0, t2.getValue("A->B"))

if __name__ == "__main__":
	unittest.main()
