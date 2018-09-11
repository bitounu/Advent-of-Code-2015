myfloor = 0;
with open('day1', 'r') as myfile:
    data=myfile.read().replace('\n', '')
for i in range(0, len(data)):
	if  data[i] == '(': 
		myfloor += 1
	else:
		myfloor -= 1
print myfloor

