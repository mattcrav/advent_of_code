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
# digits = '123123'
double_digits = digits + digits
steps = len(digits) / 2

total = 0
counter = 0
for d in digits:
	if d == double_digits[counter + steps]:
		total += int(d)
	counter += 1
	
print total


		
	

			