#!/usr/bin/python

x = ['draabina', 'antylopa', 'fntstffxy', 'jksmmm', 'baaden baaden' , 'peace' , 'pees']

def vowels(line):
    t = ['a', 'e', 'i', 'o', 'u']
    f = 0
    vows = 0
    for j in range(0, len(line)):
        c   = line[j:j+1]
        if c in t:
        #    print "Vowel bo: %s" % c
            vows += 1
    if vows >= 3:
        f = 1
    return f

for i in x:
    print "%s: %d " % (i, vowels(i))
