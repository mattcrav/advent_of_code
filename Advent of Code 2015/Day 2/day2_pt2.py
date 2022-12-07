import csv
import os
from collections import Counter

path = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(path,'boxes.csv'),'r') as file:
	reader = csv.reader(file)
	boxes = []
	for r in reader:
		boxes.append(r[0])

dims = [[int(y) for y in x.split('x')] for x in boxes]

ribbon = 0
for d in dims:
	volume = d[0] * d[1] * d[2]
	smallest = min(d)
	d.remove(smallest)
	next = min(d)
	ribbon += 2 * smallest + 2 * next + volume
	
print ribbon
		

		

		


		
	

			