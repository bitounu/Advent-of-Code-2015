#!/usr/bin/python


def parseFile(plik):
    strliteral = 0
    inmem = 0
    # otwieram plik z danymi
    with open(plik, 'r') as myfile:
        for line in myfile:
#            line = line.rstrip('\r\n')
            print "line:    ", line
            print "str:  ", len(line)
            strliteral += len(line)



    print "String literals:   ", strliteral
    print "In memory:   ", inmem
    print "strliteral - inmem   ", strliteral - inmem



def check_file(x):
    """
    'Type' for argparse - checks that file exists but does not open.
    """
    if not os.path.exists(x):
        # Argparse uses the ArgumentTypeError to give a rejection message like:
        # error: argument input: x does not exist
        raise argparse.ArgumentTypeError("{0} not exists".format(x))
    return x

if __name__ == "__main__":
    import argparse, sys, os, re
    from argparse import ArgumentParser

    Druty = {}      # Slownik na nazwy drutow (globalny)
    ARCH = 65535    # najwieksza liczba jaka mozesz niesc drut (16-bitow)

    parser = ArgumentParser(description="Next script for Advent Of Code game")
    parser.add_argument("-i", "--input",
        dest="filename", required=True, type=check_file,
        help="input file for today", metavar="FILE")
    args = parser.parse_args()

    inputfile = args.filename
    parseFile(inputfile)
