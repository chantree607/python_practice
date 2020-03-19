import string

fhand = open('mbox.txt')

d = dict()

for line in fhand:
	if line.startswith('From '):
		words = line.split()
		#print(words)
		d[words[1]] = d.get(words[1], 0) + 1

for key in d:
	print(key, d[key])

max = 0
email = ''
for key in d:
	if max < d[key]:
		max = d[key]
		email = key
print(email, max)
