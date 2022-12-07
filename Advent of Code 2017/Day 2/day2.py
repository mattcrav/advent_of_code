import csv
import os
from collections import Counter

path = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(path,'spreadsheet.csv'),'r') as file:
	reader = csv.reader(file, delimiter='\t')
	boxes = []
	for r in reader:
		boxes.append(r)


checksum = 0
for r in boxes:
	row = [int(x) for x in r]
	row_sum = max(row) - min(row)
	checksum += row_sum
	
print checksum

		
	

			