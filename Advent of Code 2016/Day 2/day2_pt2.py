import csv
import os
from collections import Counter

path = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(path,'instructions.csv'),'r') as file:
	reader = csv.reader(file)
	directions = []
	for r in reader:
		directions.append(r[0])
		
# directions = [
	# 'ULL',
	# 'RRDDD',
	# 'LURDL',
	# 'UUUUD'
	# ]
pad = [
	['#','#','1','#','#'],
	['#','2','3','4','#'],
	['5','6','7','8','9'],
	['#','A','B','C','#'],
	['#','#','D','#','#']
	]
current = [2,0]
moves = {
	'U':(-1, 0),
	'L':(0, -1),
	'R':(0, 1),
	'D':(1, 0)
	}
code = []
for d in directions:
	for m in d:
		new = [current[0] + moves[m][0], current[1] + moves[m][1]]
		try:
			value = pad[new[0]][new[1]]
			if value == '#' or new[0] == -1 or new[1] == -1:
				continue
			current = new
		except IndexError:
			continue
	code.append(pad[current[0]][current[1]])

print ''.join([str(x) for x in code])
	

		


		
	

			