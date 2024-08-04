list1 = [8, 2, 3, 0, 7]
def sumOfList(list, size):
    if (size == 0):
	    return 0
    else:
    	return list[size - 1] + sumOfList(list, size - 1)

# Driver code	
total = sumOfList(list1, len(list1))

print("Sum of all elements in given list: ", total)
