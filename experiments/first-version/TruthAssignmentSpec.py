
# defines a truth-assignement so that can be used by the students and by the test


class TruthAssignment:

    def __init__(self):
        self.values=dict()

    def setValue(self,atom,value):
        self.values[atom]=value

    def getValue(self,formula):
        if (formula[1]=='&'):
            return self.values[formula[0]] * self.values[formula[2]]
        elif (formula[1]=='|'):
            return min(1,self.values[formula[0]] + self.values[formula[2]])
        else:
            return -1
