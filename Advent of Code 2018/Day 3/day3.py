import csv
import os
import re

path = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(path,'fabric.csv'),'r') as file:
	reader = csv.reader(file)
	squares = []
	for r in file.readlines():
		vals = r.replace('#','').replace(' @ ',',').replace(': ',',').replace('x',',').replace('\n','').split(',')
		squares.append([int(x) for x in vals])
	
# squares = [
	# [1,1,3,4,4],
	# [2,3,1,4,4],
	# [3,5,5,2,2]
	# ]
# all_covers = []	
# for s in squares:
	# covers = []
	# for x in range(1, s[3] + 1):
		# for y in range(1, s[4] + 1):
			# covers.append((s[1] + x, s[2] + y))	
	# all_covers.append(covers)

# matches = []
# for a in all_covers:
	# print a
	# for b in all_covers:
		# if a == b:
			# continue
		# for a2 in a:
			# if a2 in b:
				# matches.append(a2)
				
# print len(set(matches))

covers = []
for a in squares:
	for b in squares:
		if a == b:
			continue
		x_a = range(a[1] + 1, a[1] + a[3] + 1)
		x_b = range(b[1] + 1, b[1] + b[3] + 1)
		x_inter = set(x_a).intersection(x_b)
		y_a = range(a[2] + 1, a[2] + a[4] + 1)
		y_b = range(b[2] + 1, b[2] + b[4] + 1)
		y_inter = set(y_a).intersection(y_b)
		covers += [(x,y) for x in x_inter for y in y_inter]
		
# print set(covers)
print len(set(covers))
		
# for s in squares:
	# x_a = range(s[1] + 1, s[1] + s[3] + 1)
	# print x_a
		

		

		


		
	

			