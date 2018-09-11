#!/usr/bin/python

import hashlib

puzzle_input = "ckczppom"
found = 0
i = 0

while found != 1:
    #print "i:   %d" % i
    #print "input:   %s" % (puzzle_input + str(i))
    m = hashlib.md5()
    m.update( puzzle_input + str(i))
    mhash = m.hexdigest()
    #print "Hash:    %s" % (mhash)
    if mhash[:6] == "000000":
        print "Odpowiedz:   %d" % i
        break
    i += 1
