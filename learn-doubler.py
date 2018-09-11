#!/usr/bin/python

x = ['draabina', 'antylopa', 'fanatstyffaxy', 'jakasmamam', 'baaden baaden' , 'peace' , 'pees']

def doubler(line):
    f = 0
    pc = ''
    for j in range(0, len(line)):
        c   = line[j:j+1]
        if c == pc:
            print "Powtorka bo: %s == %s" % (c, pc)
            f = 1
        else:
            pc =c
    return f
for i in x:
    print "%s: %d " % (i, doubler(i))
