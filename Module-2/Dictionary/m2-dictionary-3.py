def check(dict, key):
	
	if key in dict.keys():
		print("Present, ", end =" ")
		print("value =", dict[key])
	else:
		print("Not present")

# Driver Code
dict = {'a': 100, 'b':200, 'c':300}

key = 'b'
check(dict, key)

key = 'w'
check(dict, key)
