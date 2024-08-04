string=input("Enter string:")
if string[0].lower()==string[len(string)-1].lower()=='x':
    print(string[1:len(string)-1:1])
else:
    print(string)
