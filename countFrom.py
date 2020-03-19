fname = input('Enter a file name: ')
fhand = open(fname)

counter = 0
for line in fhand:
	if line.startswith('From:'):
		words = line.split()
		print(words[1])
		counter += 1

print(counter)