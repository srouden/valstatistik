## Synopsis

This is a statistic print thingy for the swedish election result 2014. It can search and output some statistics. 

## Code Example

```
usage: valstatistik.py [-h] -t Val [-l Län] [-k Kommun] [-v Valdistrikt]
                       [-s {L,K,V}] [-p Parti] [-o format]

Statistik om valresultatet 2014 

optional arguments:
  -h, --help      show this help message and exit
  -t Val          R, L, K för att visa statistik från valet till Riksdag,
                  Landsting eller Kommun
  -l Län          Begränsa sökning till län
  -k Kommun       Begränsa sökning till kommun
  -v Valdistrikt  Begränsa sökning till valdistrikt
  -s {L,K,V}      L, K, V för att visa statistik från Län, Kommun eller
                  Valdistrikt
  -p Parti        Lista röster för parti
  -o format       Utskriftsformat [csv, plain, simple, grid, fancy_grid, pipe,
                  orgtbl, jira, presto, psql, rst, mediawiki, moinmoin,
                  youtrack, html, latex, latex_raw, latex_booktabs, textile]
```

* The statistics for the parlament election in all municipialities in all counties that match uppsala for the party PP represented in a colon separated list:

  valstatistik -t R -l Uppsala -s K -p PP -o csv

* The statistics for the municipiality election for all electiondistricts in Göteborg for the party S represented in mediawiki format: 

  valstatistik -t K -k Göteborgs -s V -p S -o mediawiki

The output formats, except csv, are from the python module tabulate.

## Motivation

There was a need to find statistics in the huge xml-files from the swedish
national electionagency. 

## Installation

Unpack or clone it in a directory and download the archive for the
electionresult 2014 from http://www.val.se/val/val2014/statistik/index.html The
needed files are slutresultat.zip och vallokal.xml. They are presumed to be
found in a subdirectory called data with the files from slutresultat.zip in
data/slutresultat

## Overall code structure

The idea is to keep this as reusable as possible so the official xml-files is
first parsed with xslt to produce a colon separated list with one record per
row. See the comment in the xslt-files for the details. To adapt this to
a different xml representation the hope is that it will be similar enough so
that only the xslt needs to be changed.

Each filetype have their own class, currently only vallokal.py and
slutresultat.py.

## Things that doesn't work

* Print statistics for several parties
* Print statistics on Län (It's in slutresultat_00X.xml
* Probably a lot more that I haven't thought of

There are probably a lot of bugs and the quality of the code can certainly be
improved.

## API Reference

No defined API yet. The classes might be useful to do something similar.

## Tests

No tests yet.

## Contributors

Stefan Roudén wrote the first version of this.

## License

GPL3 

