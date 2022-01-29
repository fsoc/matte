#!/usr/bin/python3
import time
import sys
import random

filename = str(sys.argv[1])

corr = 0
incorr = 0
problems = []

with open(filename) as f:
	for line in f:
		line = line.rstrip('\n')
		ans = eval(line)
		problems.append({'q': line, 'a': ans})

random.shuffle(problems)

begin = time.perf_counter()
for problem in problems:
	q = problem['q']
	a = problem['a']
	reply = input(q + ' = ' )
	if str(a) == reply:
		corr += 1
		print('Rätt svar')
	else:
		incorr += 1
		print('Fel svar, rätt svar är %s' % a)
end = time.perf_counter()

dur = round(end-begin)

print('Rätta svar  %s felaktiva svar %s tid %s sekunder' % (corr, incorr, dur))
