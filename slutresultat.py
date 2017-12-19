from pathlib import Path
from lxml import etree

from parse_result import parse_result
from NestedDict import NestedDict

class slutresultat(object):
    def __init__(self):
        resultXslt = "slutresultat.xslt"

        resultPath = Path('data/slutresultat')
        riksFiles = resultPath.glob('slutresultat_????R.xml')
        lanFiles = resultPath.glob('slutresultat_????L.xml')
        kommunFiles = resultPath.glob('slutresultat_????K.xml')

        rXslt = etree.parse(resultXslt)
        rTransform = etree.XSLT(rXslt)

        resultdb = NestedDict()
        for f in kommunFiles:
            #print('-------------')
            rDom = etree.parse(str(f))
            rTrans = str(rTransform(rDom))
            #print(rTrans)
            #print('-------------')

            resultdb = parse_result(rTrans, resultdb)
            #pp.pprint(resultdb)

        #print('-------------')
        #pp.pprint(resultdb)

        return resultdb


