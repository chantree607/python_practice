fhand = open('mbox-short.txt')
count = 0
summ = 0
for line in fhand:
	if line.startswith('X-DSPAM-Confidence:'):
		count += 1
		tmp = line.find(':')
		tmp += 2
		summ += float(line[tmp:])
print(summ)
print(count)
print(summ/count)