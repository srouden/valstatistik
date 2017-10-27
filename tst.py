#!/usr/bin/env python

from lxml import etree

kKod="1082"
edKod=kKod+"0515"

dataPrefix = 'data'
cFileName = dataPrefix + '/slutresultat/slutresultat_' + kKod + 'L.xml'
mFileName = dataPrefix + '/slutresultat/slutresultat_' + kKod + 'K.xml'

print('cFilename: ', cFileName)
print('mFilename: ', mFileName)
ctree = etree.parse(cFileName)
mtree = etree.parse(mFileName)

xpath = '//VALDISTRIKT[@KOD="' + edKod + '"]//GILTIGA[@PARTI="PP"]'
print(xpath)
cVotes = ctree.findall(xpath)
mVotes = mtree.findall(xpath)

for v in cVotes:
    print("C:%s:%s:%s:%s" % (edKod, v.attrib["PARTI"], v.attrib["RÖSTER"],
        v.attrib["PROCENT"]))

for v in mVotes:
    print("M:%s:%s:%s:%s" % (edKod, v.attrib["PARTI"], v.attrib["RÖSTER"],
        v.attrib["PROCENT"]))

