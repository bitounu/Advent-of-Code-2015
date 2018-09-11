#!/usr/bin/python

x = ['draaabina', 'antylopa', 'fanatstyffaxy', 'jakasmamam', 'baaden baaden' , 'peace' , 'pees', 'goooldem', 'qjhvhtzxzqqjkmpb', 'xxyxx', 'uurcxstgmygtbstg', 'ieodomkazucvgmuy']

def doubler(line):
    f = 0
    for j in range(0, len(line)):
        c   = line[j]       # wycinam kolejny znak
        if c == line[j+2:j+3]:     # sprawdzam czy znajde jeszcze takie
            print "Ten znak: '%s', a drugi dalej to '%s', a pomiedzy '%s'. Calosc: '%s'" % (c, line[j+2:j+3], line[j+1:j+2], line[j:j+3])
            f = 1
    return f

for i in x:
    print "%s: %d " % (i, doubler(i))
