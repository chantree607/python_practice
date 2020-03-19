fhand = open('mbox.txt')
count = 0
for s in fhand:
	
	s = s[:len(s)-1]
	#oder einfacher
	#s= s.rstrip()
	if s.startswith('From: '):
		print(s)
		count += 1
print('Line Count: ', count)