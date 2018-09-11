myfloor = 0
licznik = 0
with open('day1', 'r') as myfile:
    data=myfile.read().replace('\n', '')
for i in range(0, len(data)):
	licznik += 1
	if  data[i] == '(': 
		myfloor += 1
	else:
		myfloor -= 1
	if myfloor == -1:
		print licznik
		quit()
