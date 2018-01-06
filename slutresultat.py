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

    def parse_result(self, r, result):
        #print("parse_result")
        with io.StringIO(r, newline='') as rf:
            reader = csv.reader(rf, delimiter=':', skipinitialspace=True)
            for row in reader:
                #print(row)
                if len(row) < 4:
                    pass
                elif row[0] == 'K':
                    result[row[1]] = { 
                        'type': 'K', 
                        'id': row[1],
                        'name': row[2], 
                        'votes': row[3],
                        'pct': '-'
                        }
                elif row[0] == 'KR':
                    result[row[1]][row[2]] = { 
                        'type': 'KR', 
                        'id': row[1],
                        'party': row[2], 
                        'votes': row[3], 
                        'pct': row[4] 
                        }
                elif row[0] == 'V':
                    result[row[1]]['vallokal'] = { 
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
            try:
                if party == None:
                    v = self.resultdb[code]
                else:
                    v = self.resultdb[code][party]
                if v != {}:  # NestedDict gives an empty dict if the key is not found
                    votes.append(v)
            except:
                pass

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
            return '-'

    def get_pct(self, vote):
        try:
            return vote['pct']
        except:
            return '-'
