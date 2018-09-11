#!/usr/bin/python

import sys, getopt
from copy import deepcopy
vowels = ['a','e','i','o','u']

# sprawdzam ktore linie zawieraja ciagi z listy t
def cut2(line):
    t = ['ab', 'cd', 'pq', 'xy']
    f = 0
    for j in range(0, len(line)):
        c = line[j:j+2]
        if c in t:
            f = 1 # ta linia nie jest cacy
    return f

# sprawdzam ktore linie zawieraja podwojna litere
def doubler(line):
    f = 0
    pc = '' # poprzedni znak
    for j in range(0, len(line)):
        c   = line[j:j+1]
        if c == pc:
            f = 1 # ta linia jest cacy
        else:
            pc =c
    return f

def vowels(line):
    t = ['a', 'e', 'i', 'o', 'u']
    f = 0
    vows = 0
    for j in range(0, len(line)):
        c   = line[j:j+1]
        if c in t:
            vows += 1
    if vows >= 3:
        f = 1
    return f

def cacy(plik):
    i = 0
    cacy = 0
    #adresy.append(deepcopy(currAdr)) # pierwszy adres jest pierwszy
    # otwieram plik z danymi
    with open(plik, 'r') as myfile:
        for line in myfile:
            i += 1
            if not cut2(line):
                if doubler(line):
                    if vowels(line):
                        #print "Linia %d = %s" % (i, line)
                        cacy += 1
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

