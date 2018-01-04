#!/usr/bin/python

import argparse
import sys

import vallokal
import slutresultat

def getargs():
    argparser = argparse.ArgumentParser('Statistik om valresultatet 2014')
    argparser.add_argument('-t', metavar='Val', choices=['R', 'L', 'K'], \
            type=str, required=True, \
            help='R, L, K för att visa statistik från valet ' + \
            'till Riksdag, Landsting eller Kommun')
    argparser.add_argument('-l', metavar="Län", type=str, \
            help='Begränsa sökning till län')
    argparser.add_argument('-k', metavar='Kommun', type=str, \
            help='Begränsa sökning till kommun')
    argparser.add_argument('-v', metavar='Valdistrikt', type=str, \
            help='Begränsa sökning till valdistrikt')
    argparser.add_argument('-s', choices=['L', 'K', 'V'], type=str, \
            help='L, K, V för att visa statistik från Län, Kommun eller Valdistrikt')
    argparser.add_argument('-p', metavar='Parti', type=str, \
            help='Lista röster för parti')
    #argparser.add_argument('-l', help='Lista kända objekt')

    args = argparser.parse_args()

    return args


def getcodes(info, args):
    result = []
    if args.l is not None:
        lCode = info.search(lan=args.l, get=args.s)
        result += lCode
    if args.k is not None:
        kCode = info.search(kommun=args.k, get=args.s)
        result += kCode
    if args.v is not None:
        vCode = info.search(valdistrikt=args.v, get=args.s)
        result += vCode

    #print(result)
    return result

def getvotes(codes, stats, party):
    votes = stats.getvotes(codes, party)
    return votes

def getstats(info, stats, args):
    codes = getcodes(info, args)
    votes = getvotes(codes, stats, args.p)
    return votes

def printstats(info, stats, votes):
    #print(info, stats, votes)
    for vote in votes:
        if vote != {}:
            id = stats.get_id(vote)
            name = info.get_name(id)
            numVotes = stats.get_votes(vote)
            pctVotes = stats.get_pct(vote)

            print("{0}\t\t{1}\t{2}".format(name, numVotes, pctVotes))



def main():
    args = getargs()
    #print(args)
    info = vallokal.vallokal()
    stats = slutresultat.slutresultat(args.t)
    #print(info, stats)
    #sys.exit(0)
    votes = getstats(info, stats, args)
    printstats(info, stats, votes)

if __name__ == '__main__':
    main()
