import string

try:
	fhand = open('romeo.txt')
except:
	print('File cannot be opened')

d = dict()
for line in fhand:
	line = line.rstrip()
	line = line.translate(line.maketrans('', '', string.punctuation))
	line = line.lower()
	words = line.split()
	for word in words:
		d[word] = d.get(word, 0) + 1

for key in d:
	print(key, d[key])
