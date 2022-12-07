import csv
import os
from collections import Counter

path = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(path,'directions.csv'),'r') as file:
	reader = csv.reader(file)
	for r in reader:
		# print [len(x) for x in r]
		directions = [(x.strip()[0],int(x.strip()[1:])) for x in r]
	
# directions = [('R',8),('R',4),('R',4),('R',8)]
# print directions
x = 0
y = 0
stops = [(0, 0)]
dirs = {0:'N',1:'E',2:'S',3:'W'}
dir = 0
success = False
for d in directions:
	if d[0] == 'R':
		dir += 1
	if d[0] == 'L':
		dir -= 1
	if dir == -1:
		dir = 3
	if dir == 4:
		dir = 0
	if dirs[dir] == 'N':
		for z in range(1,d[1]+1):
			stops.append((y + z,x))
		y += d[1]
	if dirs[dir] == 'E':
		for z in range(1,d[1]+1):
			stops.append((y,x + z))
		x += d[1]
	if dirs[dir] == 'S':
		for z in range(1,d[1]+1):
			stops.append((y - z, x))
		y -= d[1]
	if dirs[dir] == 'W':
		for z in range(1,d[1]+1):
			stops.append((y,x - z))
		x -= d[1]
	counter = Counter(stops)
	for c in counter:
		if counter[c] == 2:
			print c
			print abs(c[0]) + abs(c[1])
			success = True
	if success == True:
		break
	# print stops
	# print dir, x, y
		


		
	

			