# Methodology

# Given we have a binary number: 1 1 0 0 1 0
#there is a sequence		   32 16 8  4 2  1

# Formular for this sequence is a*r^n, where a=1 and r=2 and n=number of digits in the binary entry
# Lastly, we add all the sequence value where the corresponding binary is '1': 110010 = 50

def binary_to_decimal():
	y = input('Enter any binary digit >')
	final_answer,binary_value,sequence = [], [], []

	[binary_value.append(val) for val in y]

	[sequence.append(pow(1*2, t)) for t in range(0,len(y))]

	binary_value.reverse()
	indexes = [index for index in range(len(binary_value)) if binary_value[index] == '1']
	
	for val in indexes:
		final_answer.append(sequence[val])
	
	print(f'{y} to decimal is: {sum(final_answer)}')

def decimal_to_binary():
	y = int(input('Enter any decimal digit > '))
	y = 456
	print(f'{y} to binary is: {bin(y)}')

def start():
	action = input('''What action would you like to perform: 
1. Binary to Decimal
2. Decimal to Binary
> ''')
	if action == '1':
		binary_to_decimal()
	elif action == '2':
		decimal_to_binary()
	else:
		print('\aInvalid input!!')
		quit()

start()