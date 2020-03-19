fhand = open('words.txt')
words2Dict = dict()

for line in fhand:
	words = line.split()
	for word in words:
		words2Dict[word] = ''

print(words2Dict)

if 'Writing' in words2Dict:
	print('yes')