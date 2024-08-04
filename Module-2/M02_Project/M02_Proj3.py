dict={'Krishna':[67,68,69],'Arjun':[70,98,63],'Malika':[52,56,60]}
key=input('Enter a name: ')
sum=0
if key in dict.keys():
    #print(dict[key])
    for i in range(0,len(dict[key])):
        sum+= dict[key][i]
print('Average percentage marks: ',sum/3)    

          