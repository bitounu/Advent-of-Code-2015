#!/usr/bin/python

# Zdawaloby sie, ze to latwe zadanie i bedace zmodyfikowana
# kopia zadania z dnia 6.
# Najbardziej pracochlonna bedzie funkcja parsujaca.
# Wlasciwie mozna powiedziec, ze zaczynamy tworzyc cos co po odwroceniu
# moze stac sie zaczatkiem nowego jezyka programowania.
# Juz na wstepie stanalem przed dylematem czy byc leniuchem i tworzyc parser
# specyficzny do zadania czy uniwersalny. Jak uniwersalny to warto byloby
# stworzyc modul, uzywany potem w nastepnych programach.
# No, i nauka z poprzednich dni nie poszlaby na marne - nie po to wyczytywalem 
# po www, co znaczy taki zapis:
# if __name__ == "__main__":
# Wyglada na to, ze trzeba zrobic kilka przebiegow:
# 1. zebrac nazwy wszystkich drutow do slownika,
#    i zainicjalizowac te, ktore maja wartosci,
#     np. b dostaje na starcie 44430, a c = 0
# 2. ....
# Parser najpierw rozrozni ilosc elementow w linii komendy.
# Jest ich stala liczba zalezna jedynie od rodzaju operacji,
# i ma prosta zaleznosc:
# jesli elementow (slow) jest 5 to jest to rozkaz z 2 argumentami,
# w tej grupie 2 rozkazy AND oraz OR maja dwie zmienne,
# a pozostale 2 LSHIFT oraz RSHFT maja jedna zmienna oraz wartosc numeryczna.
# Jesli elementow jest 4 to argument jest jeden (NOT).


def bNOT(x):
    x = int(x)
    return ARCH - x

def bOR(x,y):
    x = int(x)
    y = int(y)
    return x | y

def bAND(x,y):
    x = int(x)
    y = int(y)
    return x & y

def bLSHIFT(x,y):
    x = int(x)
    y = int(y)
    return x << y

def bRSHIFT(x,y):
    x = int(x)
    y = int(y)
    return x >> y


def rozkazy(wL):
    print  wL
#    print "dlugosc wL: %d" % len(wL)
    # klasyfikuje na 4 i 5 slowowe rozkazy...
    if len(wL) == 2:
       # kopiuj wartosc na drut
       print "%s = %s" % (wL[0], wL[1])
    elif len(wL) == 3:
       # wykonaj bitwise NOT
#       print bNOT(wL[1])
        print "NOT"
    elif len(wL) == 4:
       # wykonaj pozostale akcje
       if wL[1] == 'OR':
            print "OR"
#           bOR( wL[0], wL[2] )
       elif wL[1] == 'AND':
            print "AND"
#           bAND( wL[0], wL[2] )
       elif wL[1] == 'LSHIFT':
            print "LSHIFT"
#           bLSHIFT( wL[0], wL[2] )
       elif wL[1] == 'RSHIFT':
            print "RSHIFT"
#           bRSHIFT( wL[0], wL[2] )

def parseFile(plik):
# slownik kable na niepowtarzalne nazwy kabli
    kable = {}
    # otwieram plik z danymi
    with open(plik, 'r') as myfile:
        for line in myfile:
            line = line.rstrip('\r\n')
            wL = re.sub("[^\w]", " ",  line).split()    # dziele linie na tablice slow
#            print "wL:  ", wL
            for kabel in wL:
                # nazwa kabla nie jest operacja ani liczba
                if kabel not in ('AND','OR','LSHIFT','RSHIFT','NOT') and not kabel.isdigit():
#                    print "kabel:   ", kabel
                    # inicjuje kable z pustymi wartosciami
                    kable.update({kabel:''})
    print kable
#            rozkazy(wL)


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
