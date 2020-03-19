fhand = open('romeo.txt')
res = list()
for line in fhand:
	words = line.split()
	for word in words:
		if len(res) == 0:
			res.append(word)
			continue
		isThere = 0
		for elem in res:
			if word == elem:
				isThere = 1
		if isThere == 0:
			res.append(word)
res.sort()
print(res)