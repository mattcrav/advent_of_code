import csv
import os
from collections import Counter

path = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(path,'floors.csv'),'r') as file:
	reader = csv.reader(file)
	for r in reader:
		floors = r[0]

counter = 1
floor = 0
for f in floors:
	if f == '(':
		floor += 1
	if f == ')':
		floor -= 1
	if floor < 0:
		print counter
		break
	counter += 1
	
print floor
	
		

		

		


		
	

			