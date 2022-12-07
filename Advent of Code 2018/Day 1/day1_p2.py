import csv
import os

path = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(path,'freq.csv'),'r') as file:
	reader = csv.reader(file)
	freqs = []
	for r in reader:
		freqs.append(int(r[0]))
		
val = 0
results = []
repeat = None
while repeat is None:
	for f in freqs:
		val += f
		if val in results:
			repeat = val
			break
		else:
			results.append(val)
print repeat