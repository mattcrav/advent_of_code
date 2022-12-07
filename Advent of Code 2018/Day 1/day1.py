import csv
import os

path = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(path,'freq.csv'),'r') as file:
	reader = csv.reader(file)
	val = 0
	for r in reader:
		freq = int(r[0].replace('+',''))
		val += freq
print val