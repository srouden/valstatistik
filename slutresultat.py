import io
import csv
from pathlib import Path
from lxml import etree
#import pprint

from NestedDict import NestedDict

class slutresultat(object):
    def __init__(self, type):
        #self.pp = pprint.PrettyPrinter()
        resultXslt = "slutresultat.xslt"

        resultPath = Path('data/slutresultat')
        #riksFiles = resultPath.glob('slutresultat_????R.xml')
        #lanFiles = resultPath.glob('slutresultat_????L.xml')
        #kommunFiles = resultPath.glob('slutresultat_????K.xml')
        files = resultPath.glob('slutresultat_????' + type + '.xml')

        rXslt = etree.parse(resultXslt)
        rTransform = etree.XSLT(rXslt)

        self.resultdb = NestedDict()
        for f in files:
            #print('Parsing ', f)
            #print('-------------')
            rDom = etree.parse(str(f))
            rTrans = str(rTransform(rDom))
            #print(rTrans)
            #print('-------------')

            self.resultdb = self.parse_result(rTrans, self.resultdb)
        #self.pp.pprint(self.resultdb)

        #print('-------------')
        #pp.pprint(resultdb)

    def parse_result(self, r, result):
        with io.StringIO(r, newline='') as rf:
            reader = csv.reader(rf, delimiter=':', skipinitialspace=True)
            for row in reader:
                if len(row) < 4:
                    pass
                elif row[0] == 'K':
                    result[row[1]] = { 
                            'type': 'K', 
                            'id': row[1],
                            'name': row[2], 
                            'votes': row[3] 
                            }
                elif row[0] == 'V':
                    result[row[1]]['lokal'] = { 
                            'type': 'V', 
                            'id': row[1],
                            'name': row[2], 
                            'votes': row[3] 
                            }
                elif row[0] == 'R':
                    result[row[1]][row[2]] = { 
                            'type': 'R', 
                            'id': row[1],
                            'party': row[2], 
                            'votes': row[3], 
                            'pct': row[4] 
                            }
                else:
                    pass

        return result

    def getdb(self):
        return self.resultdb

    def search(self):
        pass

    def getvotes(self, codes, party=None):
        votes = []
        for code in codes:
            if party == None:
                votes.append(self.resultdb[code])
            else:
                votes.append(self.resultdb[code][party])

        #self.pp.pprint(votes)
        return votes

    def get_id(self, vote):
        try:
            return vote['id']
        except:
            return None

    def get_votes(self, vote):
        try:
            return vote['votes']
        except:
            return None

    def get_pct(self, vote):
        try:
            return vote['pct']
        except:
            return None
