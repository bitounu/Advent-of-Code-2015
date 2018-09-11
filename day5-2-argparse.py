#!/usr/bin/python


def doubler(line):
    nice = 0
    for j in range(0, len(line)):
        c   = line[j:j+2]                   # wycinam 2 znaki
        if c in line[j+2:]:                 # sprawdzam czy znajde jeszcze takie
            pozycja = line[2:].find(c) + 2  # pozycja powtorki
#            print "W linii '%s' ciag: '%s' pojawia sie jeszcze na pozycji: %d" % (line, c, pozycja)
            print line
            nice = 1
            return nice

def doubler2(line):
    nice = 0
    for j in range(0, len(line)):
        c   = line[j]       # wycinam kolejny znak
        if c == line[j+2:j+3]:     # sprawdzam czy znajde jeszcze takie
#            print "W linii %s Ten znak: '%s', a drugi dalej to '%s', a pomiedzy '%s'. Calosc: '%s'" % (line, c, line[j+2:j+3], line[j+1:j+2], line[j:j+3])
            nice = 1
            return nice

def cacy(plik):
    faza1 = 0
    cacy = 0
    # otwieram plik z danymi
    with open(plik, 'r') as myfile:
        for line in myfile:
            line = line.rstrip('\r\n')
#            print line
            if doubler(line):
                faza1 += 1
                if doubler2(line):
                   # print "Linia %d = %s" % (i, line)
                    cacy += 1
    print "faza1 = %d" % faza1
    print "Linii, ktore sa cacy jest: %d" % cacy
            
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
    import argparse, sys, os
    from argparse import ArgumentParser

    parser = ArgumentParser(description="Next script for Advent Of Code game")
    parser.add_argument("-i", "--input",
        dest="filename", required=True, type=check_file,
        help="input file for today", metavar="FILE")
    args = parser.parse_args()

    inputfile = args.filename
    cacy(inputfile)
