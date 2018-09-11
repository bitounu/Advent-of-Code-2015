myOrder = 0
# licze ilosc papieru 
def paperBox(l,w,h):
	pow = l+l+w+w + l*w*h
	return pow
with open('day2', 'r') as myfile:
    data=myfile.read()
data = data.split('\n')
for i in range(0, len(data)-1):
	data2 = data[i].split('x')
	data3 = eval(str(data2).replace("'",""))
	data4 = sorted(data3)
	data5 = paperBox( int(data4[0]), int(data4[1]), int(data4[2]))
	myOrder += data5
print "Order: %d" % myOrder
