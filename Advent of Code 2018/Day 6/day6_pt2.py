import csv
import os
from datetime import datetime
from collections import Counter

path = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(path,'prod.csv'),'r') as file:
	lines = []
	for r in file.readlines():
		lines.append([int(x) for x in r.split(',')])

start = [min([x[0] for x in lines]), min([x[1] for x in lines])]
end = [max([x[0] for x in lines]), max([x[1] for x in lines])]
# print start, end

results = []
for y in range(start[0], end[0]+2):
	row = []
	# print 'hello'
	for x in range(start[1], end[1]):
		total_dist = 0
		for p in lines:
			total_dist += abs(x-p[0]) + abs(y-p[1])
		# print x, y, total_dist
		if total_dist < 10000:
			row.append('#')
		else:
			row.append('.')
	results.append(row)

# for r in results:
	# print r
# totals = {}
# edges = results[0] + results[-1]
area = 0	
for row in results:
	# edges.append(row[0])
	# edges.append(row[-1])
	for col in row:
		if col == '#':
			area += 1
# print set(edges)

print area
# max_area = 0
# for t in totals:
	# if t not in edges:
		# if totals[t] > max_area:
			# max_area = totals[t]
# print max_area
		
		
			
		


		
	


		

		


		
	

			