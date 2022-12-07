import csv
import os
from collections import Counter

path = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(path,'text.csv'),'r') as file:
	reader = csv.reader(file)
	boxes = []
	for r in reader:
		boxes.append(r[0])

# a = 'abcde'
# b = 'abzde'
# boxes = [a, b]
# print [x for x in zip(a,b) if x[0] != x[1]]

for a in boxes:
	for b in boxes:
		zipped = zip(a,b)
		diff = [x for x in zipped if x[0] != x[1]]
		if len(diff) == 1:
			index_diff = zipped.index(diff[0])
			print a[:index_diff] + a[index_diff+1:]
			break
		
	

			