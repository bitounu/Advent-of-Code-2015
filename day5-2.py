#!/usr/bin/python

import sys, getopt

def doubler(line):
    nice = 0
    for j in range(0, len(line)):
        c   = line[j:j+2]       # wycinam 2 znaki
        if c in line[j+3:]:     # sprawdzam czy znajde jeszcze takie
            print "W linii '%s' ciag: '%s' pojawia sie jeszcze tu: %s" % (line, c, line[j+1:])
            nice = 1
    return nice

def doubler2(line):
    nice = 0
    for j in range(0, len(line)):
        c   = line[j]       # wycinam kolejny znak
        if c == line[j+2:j+3]:     # sprawdzam czy znajde jeszcze takie
            print "Ten znak: '%s', a drugi dalej to '%s', a pomiedzy '%s'. Calosc: '%s'" % (c, line[j+2:j+3], line[j+1:j+2], line[j:j+3])
            nice = 1
    return nice

def cacy(plik):
    faza1 = 0
    cacy = 0
    # otwieram plik z danymi
    with open(plik, 'r') as myfile:
        for line in myfile:
            line = line.rstrip('\r\n')
            if doubler(line):
                print line
                faza1 += 1
                if doubler2(line):
                    #print "Linia %d = %s" % (i, line)
                    cacy += 1
    print "faza1 = %d" % faza1
    print "Linii, ktore sa cacy jest: %d" % cacy
            

def main(argv):
    inputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile="])
    except getopt.GetoptError:
        print 'program -i <inputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'program -i <inputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
            cacy(inputfile)

if __name__ == "__main__":
    main(sys.argv[1:])

