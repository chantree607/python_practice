import string

fhand = open('romeo.txt')

d = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('','',string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        d[word] = d.get(word,0) + 1

words = list()

for key, value in list(d.items()):
    words.append((value,key))

words.sort(reverse=True)
for val, key in words:
    print(val, key)


