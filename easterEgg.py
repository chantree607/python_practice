fname = input('Enter the file name: ')

if fname == 'na na boo boo':
	print('NA NA BOO BOO TO YOU - You have been punk')
else:
	try:
		fhand = open(fname)
		count = 0
		for i in fhand:
			count+=1
		print(count)
	except:
		print('the file doesnt exist')