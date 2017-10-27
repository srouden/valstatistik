from lxml import etree

class Votes(object):
    def __init__(self):
        self.party = ''
        self.votes = ''
        self.procent = ''

    def __init__(self, votenode):
        self.party = votenode.attrib["PARTI"]
        self.votes = votenode.attrib["RÖSTER"]
        self.procent = votenode.attrib["PROCENT"]

    def Party(self):
        return self.party

    def Count(self):
        return self.votes

    def Procent(self):
        return self.procent

    def __str__(self):
        #str = "Votes"
        str = "Votes(%s): %s(%s%%)\n" % (self.party, self.votes, self.procent)
        return str

    __repr__ = __str__
