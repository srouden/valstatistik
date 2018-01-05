#!/usr/bin/python

import argparse
import sys
from tabulate import tabulate

import vallokal
import slutresultat

def getargs():
    argparser = argparse.ArgumentParser(description='Statistik om valresultatet 2014')

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
    argparser.add_argument('-o', metavar='format', choices=['csv', 'plain', \
        'simple', 'grid', 'fancy_grid', 'pipe', 'orgtbl', 'jira', 'presto', \
        'psql', 'rst', 'mediawiki', 'moinmoin', 'youtrack', 'html', 'latex', \
        'latex_raw', 'latex_booktabs', 'textile'], default='csv', type=str, \
        help='Utskriftsformat [csv, plain, simple, grid, fancy_grid, \
        pipe, orgtbl, jira, presto, psql, rst, mediawiki, moinmoin, \
        youtrack, html, latex, latex_raw, latex_booktabs, textile]')
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
    result = []
    for vote in votes:
        if vote != {}:
            id = stats.get_id(vote)
            name = info.get_name(id)
            numVotes = stats.get_votes(vote)
            pctVotes = stats.get_pct(vote)

            result.append([name, numVotes, pctVotes])

    return result

def printcsv(votes, how, args):
    for v in votes:
        print(':'.join(v))

def printtab(votes, how, args):
    if args.s == 'K':
        region = 'Kommun'
    elif args.s == 'V':
        region = 'Valdistrikt'

    headers = [region, "Röster", "Procent"]

    print(tabulate(votes, headers=headers, tablefmt=how))

def main():
    args = getargs()
    #print(args)
    info = vallokal.vallokal()
    stats = slutresultat.slutresultat(args.t)
    votes = getstats(info, stats, args)
    if args.o == 'csv':
        printcsv(votes, args.o, args)
    else:
        printtab(votes, args.o, args)

if __name__ == '__main__':
    main()
