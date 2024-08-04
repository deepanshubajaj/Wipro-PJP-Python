string = input('Enter String: ')
j = -1
flag = 0
for i in string:
	if i != string[j]:
	    j = j - 1
	    flag = 1
	    break
	j = j - 1
if flag == 1:
	print("NO, It is not a Pallindrome")
else:
	print("Yes, It is a Pallindrome")
