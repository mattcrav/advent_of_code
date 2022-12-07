import csv
import os
from collections import Counter

path = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(path,'directions.csv'),'r') as file:
	reader = csv.reader(file)
	for r in reader:
		# print [len(x) for x in r]
		directions = [(x.strip()[0],int(x.strip()[1:])) for x in r]
	
# directions = [('R',2),('R',2),('R',2)]
print directions
x = 0
y = 0
dirs = {0:'N',1:'E',2:'S',3:'W'}
dir = 0
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
		y += d[1]
	if dirs[dir] == 'E':
		x += d[1]
	if dirs[dir] == 'S':
		y -= d[1]
	if dirs[dir] == 'W':
		x -= d[1]
	# print dir, x, y
		
print x, y
print abs(x) + abs(y)

		
	

			