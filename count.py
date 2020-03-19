def count1(name, search):
	count = 0
	for char in name:
		if char == search:
			count += 1
	print(count)

#or

def count2(name, search):
	print(name.count(search))

count1('chan yong lee', 'e' )
count2('chan yong lee', 'e' )
