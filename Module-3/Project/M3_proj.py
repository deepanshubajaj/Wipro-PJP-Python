def upperlower(string):

	upper = 0
	lower = 0

	for i in range(len(string)):
		
		# For lower letters
		if (ord(string[i]) >= 97 and
			ord(string[i]) <= 122):
			lower += 1

		# For upper letters
		elif (ord(string[i]) >= 65 and
			ord(string[i]) <= 90):
			upper += 1

	print('\nLower case characters = %s' %lower,
		'\nUpper case characters = %s' %upper)

# Driver Code
string = input('Enter string: ')
upperlower(string)
