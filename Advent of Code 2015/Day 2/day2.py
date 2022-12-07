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

surface = 0
for d in dims:
	side1 = d[0] * d[1]
	side2 = d[1] * d[2]
	side3 = d[0] * d[2]
	surface += 2 * side1 + 2 * side2 + 2 * side3 + min(side1, side2, side3)
	
print surface
		

		

		


		
	

			