#!/usr/bin/python

t = ['ab', 'cd', 'pq', 'xy']
x = 'drabina'
y = 'antylopa'
z = 'fanatstyfaxy'

def cut2(line):
    f = 0
    for j in range(0, len(line)):
        c = line[j:j+2]
        if c in t:
            f = 1 
    return f

print "x: %d " % cut2(x)
print "y: %d " % cut2(y)
print "z: %d " % cut2(z)
