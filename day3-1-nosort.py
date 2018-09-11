#!/usr/bin/python

import sys, getopt
import itertools
from copy import deepcopy
def laziMikolaj(plik):
    # pierwotna tablica zbierajaca wszystkie adresy
    adresy = [] 
    # aktualny adres Mikolaja
    currAdr= [0,0]
    # pierwszy adres jest pierwszy ;)
    adresy.append(deepcopy(currAdr))
    # tablica zliczajaca ilosc odwiedzin
    wizyty = []
    # licze sobie ile razy robil skrecal
    up=0
    right=0
    down=0
    left=0
    # ile razy odwiedzil tylko raz
    ileRaz = 1
    # otwieram plik z danymi
    with open(plik, 'r') as myfile:
        data=myfile.read().replace('\n', '')
    # iteruje znak po znaku
    for i in range(0, len(data)):
        if data[i] == '^': 
                currAdr[1]	+= 1
                up += 1
        elif data[i] == '>': 
                currAdr[0]	+= 1
                right += 1
        elif data[i] == 'v': 
                currAdr[1]	-= 1
                down += 1
        elif data[i] == '<': 
                currAdr[0]	-= 1
                left += 1
    #	print "i = %d" % i
    #	print currAdr
    # zbieram aktualne adresy do glowej tablicy
        adresy.append(deepcopy(currAdr))
    unique = [k for k,g in itertools.groupby(sorted(adresy))]
    #print "Adresy: %s" % adresy
    print "Adresy ma %s elementow" % len(adresy)
    print "Up: %s" % up
    print "Right: %s" % right
    print "Down: %s" % down
    print "Left: %s" % left
    print "Pojedynczych prezentow bylo: %d" % len(unique)

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
            laziMikolaj(inputfile)
        else:
            print 'program  -i <inputfile>'
            

if __name__ == "__main__":
    main(sys.argv[1:])



