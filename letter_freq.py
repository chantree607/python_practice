import string

fhand = open('romeo.txt')

d = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('','',string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        for c in word:
            d[c] = d.get(c,0) + 1

l = list()
for key, val in list(d.items()):
    l.append((val, key))
l.sort(reverse=True)

for val, key in l:
    print(key, val)