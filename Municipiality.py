from lxml import etree

class Municipiality(object):
    def __init__(self):
        self.id = 0
        self.name = ''
        self.total_votes = 0
        self.electionDistricts = {}
        self.cntrl_votes = {}

    def __init__(self, m):
        self.id = m.attrib["KOD"]
        self.name = m.attrib["NAMN"]
        try:
            self.total_votes = m.attrib["RöSTER"]
        except:
            pass
        self.electionDistricts = {}
        self.cntrl_votes = {}

    def add_electionDistrict(self, electionDistrict):
        self.electionDistricts[electionDistrict.kod()] = electionDistrict

    def add_cntrl_votes(self, area, party, votes):
        try:
            self.cntrl_votes[area][party] = votes
        except:
            self.cntrl_votes[area] = {}
            self.cntrl_votes[area][party] = votes

    def kod(self):
        return self.id

    def name(self):
        return self.name

    def total_votes(self, total_votes=0):
        self.total_votes = total_votes

    def define(self, ):
        pass

    def populate(self, ):
        pass

    def __str__(self):
        #print('M: ', self.id)
        str = "M %s:%s\n" % (self.id, self.name)
        for e in self.electionDistricts.keys():
            #print('ED: ', e)
            str += "   %s\n" % (self.electionDistricts[e])
        return str

    __repr__ = __str__
