#!/usr/bin/python

import vallokal
import slutresultat

def getinfo():
    return(vallokal.vallokal(), slutresultat.slutresultat())

def getargs():
    return args

def getstats():
    return stats

def printstats():

def main():
    args = getargs()
    info = getinfo()
    stats = getstats(info, args)
    printstats(stats)
