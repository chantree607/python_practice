def maxInArray(values):
	largest = None
	for value in values:
		if largest is None or largest < value:
			largest = value
	print(largest)

maxInArray([1,2,3,4,5,6])