import csv
import os
from collections import Counter

path = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(path,'digits.csv'),'r') as file:
	reader = csv.reader(file)
	boxes = []
	for r in reader:
		boxes.append(r[0])
digits = boxes[0]

last_val = None
total = 0
for d in digits:
	if d == last_val:
		total += int(d)
	last_val = d
	
if digits[0] == digits[-1]:
	total += int(digits[0])

print total


		
	

			