dict1 = {1:10, 2:20}
dict2 = {3:30, 4:40}
dict3 = {5:50, 6:60}
print("\nDictionary")
print(dict1)
print(dict2)
print(dict3)
print("\nDictionary after concatenating:")
dict1.update(dict2)
dict1.update(dict3)
print(dict1)