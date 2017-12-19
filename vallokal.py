from lxml import etree
import pprint

from parse_vallokal import parse_vallokal

class vallokal(object):
    def __init__(self):
        pp = pprint.PrettyPrinter()

        vallokalFile = "data/vallokal.xml"
        vallokalXslt = "vallokal.xslt"

        vlDom = etree.parse(vallokalFile)
        vlXslt = etree.parse(vallokalXslt)

        vlTransform = etree.XSLT(vlXslt)
        vlTrans = str(vlTransform(vlDom))
        #print(vlTrans)
        #print('-------------')

        vallokaldb = parse_vallokal(vlTrans)
        #pp.pprint(vallokaldb)

        return vallokaldb

