#!/usr/bin/env python

from lxml import etree

from Country import Country
from County import County
from Municipiality import Municipiality
from ElectionDistrict import ElectionDistrict
from Votes import Votes

# rostlokal.xml
# result
# { lan [] => 
#   { kod,
#     namn,
#     kommun [] =>
#     { kod,
#       namn,
#       rostningslokal [] =>
#       { kod,
#         namn
#       }
#     }
#   }
# }
#
#                           
# ElementPath
#   'LÄN' -> lkod, lnamn
#   'LÄN[@KOD=lkod]/KOMMUN' -> kkod, knamn
#   'LÄN[@KOD=lkod]/KOMMUN[@KOD=kkod]/RÖSTNINGSLOKAL' -> rkod, rnamn

# utlmynd.xml
# result
# { land [] => 
#   { kod,
#     namn,
#     institution [] =>
#     { namn,
#     }
#   }
# }
#
#                           
# ElementPath
#   'LAND' -> lkod
#   'LAND[@KOD=lkod]/INSTITUTION' -> instnamn

# vallokal.xml
# result
# { lan [] => 
#   { kod,
#     namn,
#     kommun [] =>
#     { kod,
#       namn,
#       valdistrikt [] =>
#       { kod,
#         namn
#       }
#     }
#   }
# }
#
#                           
# ElementPath
#   'LÄN' -> lkod, lnamn
#   'LÄN[@KOD=lkod]/KOMMUN' -> kkod, knamn
#   'LÄN[@KOD=lkod]/KOMMUN[@KOD=kkod]/VALDISTRIKT' -> vkod, vnamn

def populate(dataPrefix):
    vallokal = dataPrefix + '/vallokal.xml'
    ptree = etree.parse(vallokal)
    country = Country()
    cs = ptree.xpath('LÄN')
    for c in cs:
        county = County(c)
        country.add_county(county)
        cKod = county.kod()

        ms = ptree.xpath('LÄN[@KOD="' + cKod + '"]/KOMMUN')
        for m in ms:
            municipiality = Municipiality(m)
            mKod = municipiality.kod() 
            county.add_municipiality(municipiality)
            cFileName = dataPrefix + '/slutresultat/slutresultat_' + cKod + mKod + 'L.xml'
            mFileName = dataPrefix + '/slutresultat/slutresultat_' + cKod + mKod + 'K.xml'

            #print('cFilename: ', cFileName)
            #print('mFilename: ', mFileName)
            try:
                ctree = etree.parse(cFileName)
            except:
                pass
            try:
                mtree = etree.parse(mFileName)
            except:
                pass

            countyXpath = 'LÄN[@KOD="' + cKod + '"]'
            countTot = ctree.xpath(countyXpath)

            for count in countTot:
                county.complete(count)

            munXpath = 'KOMMUN[@KOD="' + mKod + '"]'
            muns = mtree.xpath(munXpath)

            for mun in muns:
                municipiality.complete(mun)

            pXpath = 'LÄN[@KOD="' + cKod + '"]/KOMMUN[@KOD="' + mKod + '"]/VALDISTRIKT'
            vs = ptree.xpath(pXpath)

            for v in vs:
                electionDistrict = ElectionDistrict(v)
                edKod = electionDistrict.kod() 
                municipiality.add_electionDistrict(electionDistrict)

                #xpath = '//VALDISTRIKT[@KOD="' + cKod + mKod + edKod + '"]//GILTIGA[@PARTI="PP"]'
                cntrlSumXpath = 'KOMMUN/GILTIGA | KOMMUN/ÖVRIGA_GILTIGA/GILTIGA'
                votesXpath = '//VALDISTRIKT[@KOD="' + cKod + mKod + edKod + '"]//GILTIGA'
                #print(xpath)
                try:
                    cVotes = ctree.xpath(votesXpath)
                    cCntrlSumVotes = ctree.xpath(cntrlSumXpath)
                except:
                    cVotes = []
                    cCntrlSumVotes = []
                try:
                    mVotes = mtree.xpath(votesXpath)
                    mCntrlSumVotes = mtree.xpath(cntrlSumXpath)
                except:
                    mVotes = []
                    mCntrlSumVotes = []

                #if cKod + mKod + edKod == "10820515":
                #    print(mVotes)

                for v in cVotes:
                    votes = Votes(v)
                    print("C:%s%s%s:%s:%s:%s" % (cKod, mKod, edKod,
                        votes.Party(), votes.Count(), votes.Procent()))
                    electionDistrict.add_votes('County', votes.Party(), votes)
                for v in mVotes:
                    votes = Votes(v)
                    print("M:%s%s%s:%s:%s:%s" % (cKod, mKod, edKod,
                        votes.Party(), votes.Count(), votes.Procent()))
                    electionDistrict.add_votes('Municipiality', votes.Party(), votes)
                for v in cCntrlSumVotes:
                    votes = Votes(v)
                    municipiality.add_cntrl_votes('County', votes.Party(), votes)
                for v in mCntrlSumVotes:
                    votes = Votes(v)
                    municipiality.add_cntrl_votes('Municipiality', votes.Party(), votes)

    return country

def validate(country):
    pass

country = populate('data')
#print(country)
