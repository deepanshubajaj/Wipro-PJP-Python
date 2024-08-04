dict={'Jeff':"Is afraid of Dogs.",'David':"Plays the piano.",'Jason':"Can fly an airplane."}
print('\nBefore Updation:')
for key,val in dict.items():
    print(key," : ",val)
print('\nAfter Updation:')
dict['Jill']="Can hula dance."
dict['Jeff']="Is afraid of heights."
for key,val in dict.items():
    print(key," : ",val)