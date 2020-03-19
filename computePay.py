def computePay(hours, rate):

	try: 
		hours = float(inp1)
	except:
		print('Error, please enter numeric input')

	try: 
		rate = float(inp2)
	except:
		print('Error, please enter numeric input')

	if(float(hours) > 40):
		res = 40*float(rate) + (float(hours) - 40)*(float(rate)*1.5)
	else:
		res = (float(hours))*(float(rate))

	print('Enter Hours: ')
	print(hours)
	

	print('Enter Rate: ')
	print(rate)
	

	print('Pay: ')
	print(res)


computePay(45, 10)


