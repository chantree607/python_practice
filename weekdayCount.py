import string

fhand = open('mbox.txt')

d = dict()

for line in fhand:
	if line.startswith('From '):
		words = line.split()
		#print(words)
		d[words[2]] = d.get(words[2], 0) + 1

print(d)
