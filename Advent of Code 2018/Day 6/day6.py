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
	for x in range(start[1], end[1]):
		# print x, y
		min_dist = 100000000
		points = []
		for p in lines:
			p_name = ','.join([str(s) for s in p])
			dist = abs(x-p[0]) + abs(y-p[1])
			# print p, dist
			if dist == min_dist:
				min_dist = dist
				points.append(p_name)
			if dist < min_dist:
				min_dist = dist
				points = [p_name]
		if len(points) > 1:
			row.append('.')
		else:
			row.append(points[0])
	results.append(row)

# for r in results:
	# print r
totals = {}
edges = results[0] + results[-1]	
for row in results:
	edges.append(row[0])
	edges.append(row[-1])
	for col in row:
		if col == '.':
			continue
		if col not in totals:
			totals[col] = 1
		else:
			totals[col] += 1
# print set(edges)

max_area = 0
for t in totals:
	if t not in edges:
		if totals[t] > max_area:
			max_area = totals[t]
print max_area
		
		
			
		


		
	


		

		


		
	

			