def ReturnString(string,n):
    new=""
    for i in range(n):
        new+=string
    return new

# Driver Code
string=input("Enter string:")
n=int(input('Enter the value of n: '))
count=0
if len(string)>=2:
    for i in string:
      count=count+1
    new=string[0:2]
print("Newly formed string is:")
print(ReturnString(new,n))