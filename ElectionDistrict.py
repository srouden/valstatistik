from lxml import etree

class ElectionDistrict(object):
    def __init__(self):
        self.id = 0
        self.name = ''
        self.total_votes = 0
        self.votes = {}

    def __init__(self, e):
        self.id = e.attrib["KOD"]
        self.name = e.attrib["NAMN"]
        try:
            self.total_votes = e.attrib["RÖSTER"]
        except:
            pass
        self.votes = {}

    def add_votes(self, voteType, voteParty, votes):
        try:
            self.votes[voteType][voteParty] = votes
        except KeyError:
            self.votes[voteType] = {}
            self.votes[voteType][voteParty] = votes

    def kod(self):
        return self.id

    def name(self):
        return self.name

    def total_votes(self, total_votes=0):
        self.total_votes = e.attrib["RÖSTER"]

    def define(self, ):
        pass

    def populate(self, ):
        pass

    def __str__(self):
        #print('ED: ', self.id)
        str = "E %s:%s\n" % (self.id, self.name)
        for r in self.votes.keys():
            for p in self.votes[r].keys():
                str += "   %s:%s:%s\n" % (r, p, self.votes[r][p])

        return str

    __repr__ = __str__
