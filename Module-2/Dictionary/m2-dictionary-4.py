Dict = {1:10,2:20,3:30,4:40,5:50}
print('Dictonary:')
# Keys alone
print('\nKeys:')
for key in Dict:
	print(key)
# Values alone
print('\nValues:')
for val in Dict.values():
	print(val)
# Keys and Values Together
print('\nKeys : Values')
for key,val in Dict.items():
    print(key," : ",val)
