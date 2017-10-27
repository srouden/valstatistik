from lxml import etree

class County(object):
    def __init__(self):
        self.id = 0
        self.name = ''
        self.municipialities = {}

    def __init__(self, c):
        self.id = c.attrib["KOD"]
        self.name = c.attrib["NAMN"]
        self.municipialities = {}

    def add_municipiality(self, municipiality):
        self.municipialities[municipiality.kod()] = municipiality

    def kod(self):
        return self.id

    def name(self):
        return self.name

    def define(self, ):
        pass

    def populate(self, ):
        pass

    def __str__(self):
        str = "C %s:%s\n" % (self.id, self.name)
        for m in self.municipialities.keys():
            str += "   %s\n" % (self.municipialities[m])
        return str

    __repr__ = __str__
