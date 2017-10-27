class Country(object):
    def __init__(self):
        self.counties = {}

    def define(self, ):
        pass

    def populate(self, ):
        pass

    def add_county(self, county):
        self.counties[county.kod()] = county

    def __str__(self):
        str = ''
        for c in self.counties.keys():
            str += "%s\n" % (self.counties[c])
        return str

    __repr__ = __str__
