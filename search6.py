fname = input('Enter the file name: ')
try:
	fhand = open(fname)
	count = 0
	for line in fhand:
		if line.startswith('Subject: '):
			count +=1
	print(count)
except:
	print("the file doesnt exist", fname)