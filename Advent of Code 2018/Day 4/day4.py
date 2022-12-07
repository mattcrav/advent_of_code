import csv
import os
from datetime import datetime
from collections import Counter

path = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(path,'times.csv'),'r') as file:
	lines = []
	for r in file.readlines():
		timestamp = datetime.strptime(r[r.index('[')+1:r.index(']')], '%Y-%m-%d %H:%M')
		lines.append([timestamp, r])
		
lines = sorted(lines, key=lambda x: x[0])

shifts = []
shift = []
for r in lines:
	timestamp = r[0]
	data = r[1]
	if 'Guard' in data:
		if len(shift) > 0:
			shifts.append(shift)
		shift = []
		num = int(data[data.index('#')+1:data.index('b')-1])
		shift.append(num)
		shift.append({x:'.' for x in range(0,60)})
	if 'wakes' in data:
		for m in range(last_row[0].minute, r[0].minute):
			shift[1][m] = '#'
	last_row = r
shifts.append(shift)

sleep_total = {}
sleep_most = {}
for s in shifts:
	if s[0] not in sleep_total:
		sleep_total[s[0]] = 0
		sleep_most[s[0]] = []
	sleep_minutes = [x for x in s[1] if s[1][x] == '#']
	sleep_count = len(sleep_minutes)
	sleep_most[s[0]] += sleep_minutes
	sleep_total[s[0]] += sleep_count

sorted_sleep_total = sorted(sleep_total, key=lambda x: sleep_total[x], reverse=True)	
sleepiest = sorted_sleep_total[0]
counter = Counter(sleep_most[sleepiest])
sleepiest_minute = counter.most_common(1)[0][0]

print sleepiest, sleepiest_minute, sleepiest * sleepiest_minute
		
	


		

		


		
	

			