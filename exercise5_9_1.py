
total = 0
count = 0
largest = None
smallest = None

inp = None

while inp != 'done':
	inp = input('Enter a number: ')
	try:
		tmp = float(inp)
		total += tmp
		count += 1
		if largest is None or tmp > largest:
			largest = tmp
		if smallest is None or tmp < smallest:
			smallest = tmp	
	except:
		print('please enter a numeric value')

print(total)
print(count)
try:
	print(total/count)
except:
	print('division by zero')	
print(largest)
print(smallest)
