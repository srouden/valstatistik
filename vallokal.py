from lxml import etree
import io
import csv
from itertools import chain
from NestedDict import NestedDict
#import pprint

class vallokal(object):
    def __init__(self):
        #self.pp = pprint.PrettyPrinter()

        vallokalFile = "data/vallokal.xml"
        vallokalXslt = "vallokal.xslt"

        vlDom = etree.parse(vallokalFile)
        vlXslt = etree.parse(vallokalXslt)

        vlTransform = etree.XSLT(vlXslt)
        vlTrans = str(vlTransform(vlDom))
        #print(vlTrans)
        #print('-------------')

        self.vallokaldb = self.parse_vallokal(vlTrans)
        #self.pp.pprint(self.vallokaldb)

        return None

    def parse_vallokal(self, vl):
        #print("parse_vallokal")
        #print(vl)
        vallokal = NestedDict()
        with io.StringIO(vl, newline='') as vlf:
            reader = csv.reader(vlf, delimiter=':', skipinitialspace=True)
            for row in reader:
                #print(row)
                if len(row) <= 1:
                    pass
                elif row[0] == 'L':
                    #print("Found Län: {0}({1})".format(row[2], row[1]))
                    vallokal[row[1]] = { 'type': 'L', 'id': (row[1],), 'name': row[2] }
                    try:
                        vallokal['l'].append(row[1])
                    except:
                        vallokal['l'] = []
                        vallokal['l'].append(row[1])
                    #print("Saved län ")
                    #self.pp.pprint(vallokal[row[1]])
                    #self.pp.pprint(vallokal['l'])
                elif row[0] == 'K':
                    #print("Found Kommun: {0}({1})".format(row[4], row[1]))
                    vallokal[row[1]] = \
                    { 'type': 'K', 'id': (row[2], row[3]), 'name': row[4] }
                    try:
                        vallokal['kl'][row[2]].append(row[3])
                    except:
                        vallokal['kl'][row[2]] = []
                        vallokal['kl'][row[2]].append(row[3])
                    #print("Saved län ")
                    #self.pp.pprint(vallokal[row[1]])
                    #self.pp.pprint(vallokal['kl'][row[2]])
                elif row[0] == 'V':
                    #print("Found Län: {0}({1})".format(row[5], row[1]))
                    vallokal[row[1]] = \
                    { 'type': 'V', 'id': (row[2], row[3], row[4]), 'name': row[5] }
                    try:
                        vallokal['vk'][row[2]+row[3]].append(row[4])
                    except:
                        vallokal['vk'][row[2]+row[3]] = []
                        vallokal['vk'][row[2]+row[3]].append(row[4])
                    #print("Saved län ")
                    #self.pp.pprint(vallokal[row[1]])
                    #self.pp.pprint(vallokal['l'])
                else:
                    pass

        return vallokal

    def getdb(self):
        return self.vallokaldb

    def search(self, lan=None, kommun=None, valdistrikt=None, get=None):
        #print("search")
        if get == None:
            return None

        db=self.vallokaldb

        ids = []
        
        #print("search: lan={0} kommun={1} valdistrikt:{2} get:{3}".format(lan, \
        #    kommun, valdistrikt, get))
        nk = filter(lambda s: all(c.isdigit() for c in s), db.keys())
        #print("db.keys(): ", db.keys())
        #print("nk: ", nk)

        for k in nk:
            #print("k: ", k)
            #print("db[k]: ")
            #self.pp.pprint(db[k])
            #print("lan={0} type={1}".format(lan, db[k]['type']))
            #print("kommun={0} type={1}".format(kommun, db[k]['type']))
            #print("valdistrikt={0} type={1}".format(valdistrikt, db[k]['type']))
            if lan and db[k]['type'] == 'L' and \
                    lan.lower() in db[k]['name'].lower():
                #print("Matched Län id=", k);
                ids.append(k)
            elif kommun and db[k]['type'] == 'K' and \
                    kommun.lower() in db[k]['name'].lower():
                #print("Matched Kommun id=", k);
                ids.append(k)
            elif valdistrikt and db[k]['type'] == 'V' and \
                    valdistrikt.lower() in db[k]['name'].lower():
                #print("Matched Valdistrikt id=", k);
                ids.append(k)

        #print("ids: ", ids)

        # Presumptions: 
        # The key in vallokaldb have all information about which Län, Kommun
        # and Valdistrikt it references.
        # The first two numbers indicates Län
        # The second pair indicates Kommun
        # The last four numbers indicates Valdistrikt
        #print("search id {0} in {1}".format(get, ids))
        result = []
        for id in ids:
            idtype = db[id]['type']
            #print("id: {0} type: {1}".format(id, idtype))
            #print("Looking at entry")
            #self.pp.pprint(db[id])

            if get == 'L':
                result.append(db[id]['id'][0])

            if get == 'K':
                if idtype == 'L':
                    ks = db['kl'][db[id]['id'][0]]
                    #print(ks)
                    kcodes = [db[id]['id'][0] + k for k in ks] 
                    #print(kcodes)
                    result += kcodes
                elif idtype == 'K' or idtype == 'V':
                    kcode = db[id]['id'][0] + db[id]['id'][1]
                    #print(kcode)
                    result.append(kcode)

            if get == 'V':
                if idtype == 'L':
                    ks = db['kl'][db[id]['id'][0]]
                    #print(ks)
                    kcodes = [db[id]['id'][0] + k for k in ks] 
                    #print(kcodes)
                    vcodes = [[kcode + v for v in db['vk'][kcode]] \
                            for kcode in kcodes]
                    #print(vcodes)
                    result += list(chain.from_iterable(vcodes))

                elif idtype == 'K':
                    kommunid = db[id]['id'][0] + db[id]['id'][1]
                    vs = db['vk'][kommunid]
                    #print(vs)
                    vcodes = [db[id]['id'][0] + db[id]['id'][1] + v for v in vs] 
                    #print(vcodes)
                    result += vcodes
                elif idtype == 'V':
                    vcode = db[id]['id'][0] + db[id]['id'][1] + db[id]['id'][2]
                    #print(vcode)
                    result.append(vcode)

        return sorted(set(result))


    def get_name(self, id):
        #print('vallokal.get_name(', id, ')')
        try:
            return self.vallokaldb[id]['name']
        except:
            return '-'

