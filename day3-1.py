#!/usr/bin/python

import sys, getopt
from copy import deepcopy

def laziMikolaj(plik):
    # pierwotna tablica zbierajaca wszystkie adresy
    adresy = [] 
    # aktualny adres Mikolaja
    currAdr= [0,0]
    adresy.append(deepcopy(currAdr)) # pierwszy adres jest pierwszy
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
    with open('day3', 'r') as myfile:
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
    # sortowanie po wspolrzednej X
    adx=sorted(adresy,key=lambda x: x[0])
    # sortowanie po wspolrzednej Y
    bdx=sorted(adx,key=lambda x: x[1])
    prevX = bdx[0][0] # poprzedniego nie ma wiec jest nim pierwszy
    prevY = bdx[0][1] # j.w.
    zmiana = 1
    for i in range(0, len(bdx)):
        x = bdx[i][0]
        y = bdx[i][1]
        if x == prevX and y == prevY:
            if zmiana == 1:
                ileRaz -= 1
                zmiana = 0
#                 print "zmiana z 1 na 0"
#             print "----------------------------------------------------------"
#             print "Obecnie:	%d:	%s" % (i, bdx[i])
#             print "Poprzednio:		%d, %d, ileRaz = %d" % (prevX, prevY, ileRaz)
        else:
            zmiana = 1
#             print "zmiana z 0 na 1"
            ileRaz += 1
#             print "----------------------------------------------------------"
#             print "Obecnie:	%d:	%s" % (i, bdx[i])
#             print "Poprzednio:	***	%d, %d, ileRaz = %d" % (prevX, prevY, ileRaz)
            prevX = x
            prevY = y
    #print "Adresy: %s" % adresy
    print "Adresy ma %s elementow" % len(adresy)
    print "Up: %s" % up
    print "Right: %s" % right
    print "Down: %s" % down
    print "Left: %s" % left
    #print "bdx: %s" % bdx
    print "Pojedynczych prezentow bylo: %d" % ileRaz

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
            laziMikolaj(inputfile)

if __name__ == "__main__":
    main(sys.argv[1:])

