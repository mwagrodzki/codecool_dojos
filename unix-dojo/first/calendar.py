with open('calendar.txt', 'r') as file:
	lines = file.readlines()

for line in lines:
	print(line.replace('\n',''))
