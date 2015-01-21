__author__ = 'Jeffrey'

class Evidence:
    def __init__(self, name, b_given_a, b_given_a_not):
        self.name = name
        self.b_given_a = b_given_a
        self.b_given_a_not = b_given_a_not

class Event:
    def __init__(self, name, prior, evidence):
        self.name = name
        self.prior = prior
        self.evidence = evidence

    def post(self):
        p_given_a = self.prior
        p_given_a_not = 1 - self.prior
        for item in self.evidence:
            p_given_a *= item.b_given_a
            p_given_a_not *= item.b_given_a_not

        return p_given_a / (p_given_a + p_given_a_not)


#to be refactored once I do all the flask stuff
#for now it just reads from a txt document
#format is Event:probability Evidence1:p_given_a:p_given_a_not Evidence2....
#return: list of event objects

def load_data_helper(line):
    line.split()
    name, prior = line[0].split(":")
    evidence = [item.split(":") for item in line[1:]]
    return [Event(name, a, a_not) for name, a, a_not in evidence]

def load_data(path):
    reader = open(path)
    return [load_data_helper(line) for line in reader]




