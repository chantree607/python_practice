try: 
	inp1 = input('Enter Hours: ')
	hours = float(inp1)
except:
	print('Error, please enter numeric input')

try: 
	inp2 = input('Enter Rate: ')
	rate = float(inp2)
except:
	print('Error, please enter numeric input')


if(float(hours) > 40):
	res = 40*float(rate) + (float(hours) - 40)*(float(rate)*1.5)
else:
	res = (float(hours))*(float(rate))

print('Pay: ' + str(res))
