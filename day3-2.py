#!/usr/bin/python
import sys, getopt
import itertools
from copy import deepcopy

def lazi(plik,start, step):
    # pierwotna tablica zbierajaca wszystkie adresy
    adresy = [] 
    # aktualny adres Mikolaja
    currAdr= [0,0]
    # pierwszy adres jest pierwszy ;)
    adresy.append(deepcopy(currAdr))
    # tablica zliczajaca ilosc odwiedzin
    wizyty = []
    # otwieram plik z danymi
    with open(plik, 'r') as myfile:
        data=myfile.read().replace('\n', '')
    # iteruje znak po znaku
    for i in range(start, len(data), step):
        if data[i] == '^': 
                currAdr[1]	+= 1
        elif data[i] == '>': 
                currAdr[0]	+= 1
        elif data[i] == 'v': 
                currAdr[1]	-= 1
        elif data[i] == '<': 
                currAdr[0]	-= 1
        # zbieram aktualne adresy do glowej tablicy
        adresy.append(deepcopy(currAdr))
    return adresy

def zlicz(lazik, adresy):
    unique = [k for k,g in itertools.groupby(sorted(adresy))]
    #print "Adresy: %s" % adresy
    print "Lazil: %s" % lazik
    print "Adresy ma %s elementow" % len(adresy)
    print "Pojedynczych prezentow bylo: %d" % len(unique)
    return len(unique)

def main(argv):
    inputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile="])
    except getopt.GetoptError:
        print 'test.py -i <inputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
            Miki    = lazi(inputfile, 0, 2)
            Robot   = lazi(inputfile, 1, 2)
            Razem   = Miki + Robot
            razem = zlicz("Razem", Razem)
            print "Razem: %d" % razem

if __name__ == "__main__":
    main(sys.argv[1:])



