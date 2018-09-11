#!/usr/bin/python


def parseFile(plik):
    wL = ''
    # otwieram plik z danymi
    with open(plik, 'r') as myfile:
        for line in myfile:
            line = line.rstrip('\r\n')
#            print line
            wL = re.sub("[^\w]", " ",  line).split()
#            print wL
#            wL = [map(int, x) for x in wL]
            if wL[0] == 'toggle':
                toggle(wL[1], wL[2], wL[4],wL[5])
            elif wL[0] == 'turn':
                if wL[1] == 'on':
                    turnOn(wL[2], wL[3], wL[5], wL[6])
                else:
                    turnOff(wL[2], wL[3], wL[5], wL[6])


def toggle(x,a,y,b):
    x = int(x)
    a = int(a)
    y = int(y)
    b = int(b)
#    print "TOGGLE x = %d, a = %d, y = %d, b = %d" % (x,a,y,b)
    for i in range(x, y+1):
        for j in range(a, b+1):
            if M[i][j] == 0:
                M[i][j] = 1
            else:
                M[i][j] = 0

def turnOn(x,a,y,b):
    x = int(x)
    a = int(a)
    y = int(y)
    b = int(b)
#    print "TURN ON x = %d, a = %d, y = %d, b = %d" % (x,a,y,b)
    for i in range(x, y+1):
        for j in range(a, b+1):
            M[i][j] = 1
	    print M

def turnOff(x,a,y,b):
    x = int(x)
    a = int(a)
    y = int(y)
    b = int(b)
#    print "TURN OFF x = %d, a = %d, y = %d, b = %d" % (x,a,y,b)
    for i in range(x, y+1):
        for j in range(a, b+1):
            M[i][j] = 0

def checkM():
    i = 0
    j = 0
    litOn = 0
    for i in range(0, len( M[i] ) ):
#        print M[i]
        for j in range(0, len( M[j] ) ):
            if M[i][j] == 1:
                litOn += 1
    print "Zapalonych: %d" % litOn



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

    w = 1000    # kolumny matrycy
    h = 1000    # rzedy matrycy
    M = [ [0 for x in range(w)] for y in range(h) ]

    parser = ArgumentParser(description="Next script for Advent Of Code game")
    parser.add_argument("-i", "--input",
        dest="filename", required=True, type=check_file,
        help="input file for today", metavar="FILE")
    args = parser.parse_args()

    inputfile = args.filename
    parseFile(inputfile)
    checkM()
