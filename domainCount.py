import string

fhand = open('mbox.txt')

d = dict()

for line in fhand:
	if line.startswith('From '):
		words = line.split()
		email = words[1]
		domain = email.split('@')[1]
		d[domain] = d.get(domain, 0) + 1

print(d)
