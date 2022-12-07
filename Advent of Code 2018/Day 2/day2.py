import csv
import os
from collections import Counter

path = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(path,'text.csv'),'r') as file:
	reader = csv.reader(file)
	freqs = []
	for r in reader:
		freqs.append(r[0])

twice = 0
thrice = 0		
for f in freqs:
	counter = Counter(f)
	if any([counter[x] == 2 for x in counter]):
		twice += 1
	if any([counter[x] == 3 for x in counter]):
		thrice += 1
print twice
print thrice
print twice * thrice		
			